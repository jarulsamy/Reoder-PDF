from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter


def generate_order(total: int):
    """Generates a page order, moving from either side inward.

    A handy default order when using a document feeder,
    and scanning doubled sided documents.

    Args:
        total: Int of total number of pages.

    Returns:
        list of page numbers in correct order.

    Raises:
        None

    Example, 10 pages.
    >>> generate_order(10)
        [0, 9, 1, 8, 2, 6, 3, 5, 4]
    """
    order = []
    i = 0
    while i < total / 2:
        order.append(i)
        order.append(total - i)
        i += 1
    return order


def reorder(filename: str, page_order=None, output_filename=None):
    """Reorder the pages in a pdf based on the specified order.

    Args:
        filename: Str path to input PDF.
        page_order: Optional parameter, listing new order of pages.
        output_filename: Str path to new PDF.

    Returns:
        None

    Raises:
        ValueError, if length of page_order != total number of pages.
    """

    if output_filename is None:
        output_filename = f"reordered_{filename}"

    output_pdf = PdfFileWriter()

    with open(filename, "rb") as readfile:
        input_pdf = PdfFileReader(readfile, strict=False)

        # indexing starts at zero.
        total = input_pdf.getNumPages()

        if page_order is not None:
            if len(page_order) != len(total):
                raise ValueError(
                    "Length of page order must equal total number of pages."
                )
        else:
            page_order = generate_order(total - 1)

        # Add pages to new pdf in correct order.
        for i in page_order:
            output_pdf.addPage(input_pdf.getPage(i))

    # Write result to file.
    with open(output_filename, "wb") as write_f:
        output_pdf.write(write_f)
