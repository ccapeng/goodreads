import math
import xml.etree.ElementTree as ET

def parse_text(xml_text):
    root = ET.fromstring(xml_text)
    result = parse_tree(root)
    return result 


def parse_tree(root):
    result = {}
    result['start'] = root.find('./search/results-start').text
    result['end'] =  root.find('./search/results-end').text
    result['total'] = root.find('./search/total-results').text
    result['totalPage'] = math.ceil(int(result['total'])/20)

    books = []
    for item in root.findall('./search/results/work'):
        id = item.find('./id').text
        title = item.find('./best_book/title').text
        author = item.find('./best_book/author/name').text
        image = item.find('./best_book/small_image_url').text
        book = {
            'id': id,
            'title': title,
            'author': author,
            'image': image
        }
        books.append(book)

    result['books'] = books
    return result


def parse_file(xml_file): 
    tree = ET.parse(xml_file)
    root = tree.getroot()
    result = parse_tree(root)
    print(result)
    
      
if __name__ == "__main__": 
    parse_file("search_result.xml") 