from Classes.Operations.DataStructures.OperationsList import OperationsList
from Classes.Operations.DataStructures.OperationsStack import OperationsStack
from Classes.Operations.DataStructures.OperationsQueue import OperationsQueue
from Classes.Operations.DataStructures.OperationsGraph import OperationsGraph
from Classes.Operations.DataStructures.OperationsTree import OperationsTree


class OperationsMain:
    def menu_DataStructures(self):
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

    def menu_Algorithms(self):
        while True:
            print("Selecciona un algoritmo de ordenamiento:")
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

