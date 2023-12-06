from Classes.Operations.OperationsList import OperationsList
from Classes.Operations.OperationsStack import OperationsStack
from Classes.Operations.OperationsQueue import OperationsQueue
from Classes.Operations.OperationsGraph import OperationsGraph
from Classes.Operations.OperationsTree import OperationsTree


if __name__ == '__main__':
    while True:
        print("Select a data structure:")
        print("1. Lists \n"
              + "2. Stacks \n"
              + "3. Queue \n"
              + "4. Trees \n"
              + "5. Graphs \n"
              + "0. Exit \n")

        try:
            option = int(input())
        except ValueError:
            OperationsList.deffault()
            continue

        if option == 1:
            OperationsList.menu_list()
        elif option == 2:
            OperationsStack.menu_stack()
        elif option == 3:
            OperationsQueue.menu_queue()
        elif option == 4:
            OperationsTree.tree_menu()
        elif option == 5:
            OperationsGraph.menu_graphs()
        elif option == 0:
            break
        else:
            OperationsList.deffault()

