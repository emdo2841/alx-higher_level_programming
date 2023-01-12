table File  5 lines (5 sloc)  195 Bytes

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def find_search(element):
        return element if element != search else replace
    return list(map(find_search, my_list))
