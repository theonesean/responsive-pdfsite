# responsive-pdfsite: the future of the web

Grandiose? I think not.

`responsive-pdfsite` (pronounced "respon-sive-pdf-site") (new name TK™) is a tool that generates responsive PDFs.

## Responsive PDFs?

Yes.

## Why?

Because I thought it would be cool.

## How?

It's a `flask` app that uses the (excellent) library `borb` to generate PDFs programmatically within Python.
Essentially, it is a webserver that serves a page that gets the viewport dimensions, sets them as cookies, and
redirects to a route that reads those cookies and generates a PDF.

## TODO

- A major challenge I've noticed so far is that, by default, Chrome's PDF viewer opens with the sidebar open.
  I'm not sure how to fix this, as it's a browser-level issue. However, this means the PDF doesn't have the opportunity
  to take up the entire viewport, even though it's sized for it. I think this issue can be ameliorated with a message on
  the page to the end-user.
- This proof-of-concept only has one page. I want to define a site structure with a database or some data representation (YAML files?)
  and maybe even have something similar to a static-site generator, but for pdfsites.
