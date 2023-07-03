import unittest
from src.pdfbotsearch.components.PDFExtractor import PDFExtractor
from src.pdfbotsearch.components.PDFExtractorEnum import PDFExtractorEnum

class TestPDFExtractor(unittest.TestCase):
    def test_extract_docs_from_PDF_with_PyPDFLoader(self):
        # Test that PyPDFLoader returns a list of documents
        file_path = "test_files/test.pdf"
        docs = PDFExtractor.extract_docs_from_PDF(file_path, PDFExtractorEnum.PyPDFLoader)
        self.assertIsInstance(docs, list)
        self.assertGreater(len(docs), 0)
        self.assertIsInstance(docs[0], str)

    def test_extract_docs_from_PDF_with_OnlinePDFLoader(self):
        # Test that OnlinePDFLoader returns a list of documents
        file_path = "test_files/test.pdf"
        docs = PDFExtractor.extract_docs_from_PDF(file_path, PDFExtractorEnum.PdfReader)
        self.assertIsInstance(docs, list)
        self.assertGreater(len(docs), 0)
        self.assertIsInstance(docs[0], str)

    def test_extract_docs_from_PDF_with_invalid_extractor_type(self):
        # Test that an invalid extractor type raises a ValueError
        file_path = "test_files/test.pdf"
        with self.assertRaises(ValueError):
            PDFExtractor.extract_docs_from_PDF(file_path, "invalid_extractor_type")

if __name__ == '__main__':
    unittest.main()