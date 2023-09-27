import re
import fitz

def find_keywords_on_page(page_text, keywords, page_num):
    results = {keyword: [] for keyword in keywords}
    sentences = page_text.split('.')
    for sentence in sentences:
        for keyword in keywords:
            if keyword.lower() in sentence.lower():
                results[keyword].append(f"Page {page_num}: {sentence.strip()}")
    return results

def search_keywords(file_path, keywords):
    pdf_document = fitz.open(file_path)
    all_results = {keyword: [] for keyword in keywords}
    
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        page_text = page.get_text()
        results = find_keywords_on_page(page_text, keywords, page_num + 1)  # Page numbers start from 1
        for keyword, sentences in results.items():
            all_results[keyword].extend(sentences)

    pdf_document.close()
    return all_results

def write_results_to_file(results, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as f:
        for keyword, sentences in results.items():
            f.write(f"Results for keyword: {keyword}\n")
            for sentence in sentences:
                f.write(f"{sentence}\n")
            f.write("\n")

def main():
    file_path = 'Chowchilla/Chowchilla_GSP_20200107_final.pdf'  # path to the big file
    keywords = ['fund', 'finance', 'financing', 'cost', 'grant', 'budget', 'million', 'dollar', 'fees', 'capital', 'rates', 'revenue', 'bond', 'loan', 'tax', 'grant']  # keywords to search
    output_file_path = 'results.txt'  # path to the output file

    results = search_keywords(file_path, keywords)
    write_results_to_file(results, output_file_path)

if __name__ == "__main__":
    main()
