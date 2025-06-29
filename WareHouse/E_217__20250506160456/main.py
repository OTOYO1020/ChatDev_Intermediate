'''
Main application file for the integer list management.
'''
from list_manager import ListManager
def main():
    Q = int(input())  # Directly read the number of queries without a prompt
    list_manager = ListManager()
    results = []
    for _ in range(Q):
        query = input().strip()
        if query.startswith('1'):
            _, x = map(int, query.split())
            list_manager.add_to_list(x)
        elif query == '2':
            if not list_manager.is_empty():
                first_value = list_manager.get_first()
                results.append(first_value)
                list_manager.remove_first()
            else:
                print("List is empty. Cannot perform operation.")
        elif query == '3':
            list_manager.sort_list()
    for result in results:
        print(result)
if __name__ == "__main__":
    main()