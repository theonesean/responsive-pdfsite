from flask import Flask, render_template, request
from flask.helpers import make_response
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
import io


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("screengrab.html")


@app.route("/<name>")
def hello_name(name):
    viewport_height = request.cookies.get("viewportHeight")
    viewport_width = request.cookies.get("viewportWidth")

    return "<p>Hello, {}! Your viewport size is {}x{}.</p>".format(
        name, viewport_width, viewport_height
    )


@app.route("/pdf/<name>.pdf")
def hello_pdf(name):
    viewport_width = request.cookies.get("viewportWidth")
    viewport_height = request.cookies.get("viewportHeight")
    if viewport_width is None or viewport_height is None:
        viewport_size = []
    else:
        viewport_size = [int(viewport_width), int(viewport_height)]

    # create an empty Document
    pdf = Document()

    # add an empty Page
    page = Page(*viewport_size)
    pdf.append_page(page)

    # use a PageLayout (SingleColumnLayout in this case)
    layout = SingleColumnLayout(page)

    # add a Paragraph object
    p = Paragraph(
            f"Hello World! Your computer screen size is {viewport_width}x{viewport_height}. Click me! I'm a link!"
        )
    layout.add(p)

    # add a link to the layout
    page.append_remote_go_to_annotation(
        p.get_bounding_box(), uri="http://localhost:5000/"
    )

    # binary_pdf = io.BytesIO()
    # PDF.dumps(binary_pdf, pdf)

    # print(binary_pdf.read())
    # print(pdf.pages)

    # response = make_response(binary_pdf.read())

    with open("test.pdf", "wb") as binary_pdf:
        PDF.dumps(binary_pdf, pdf)

    with open("test.pdf", "rb") as binary_pdf:
        response = make_response(binary_pdf.read())

    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = 'filename="%s.pdf"' % name
    return response


if __name__ == "__main__":
    app.run(debug=True)
