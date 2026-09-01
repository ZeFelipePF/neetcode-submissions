class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def add(self, val):
        new_node = Node(val)
        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = new_node

    def remove_front(self):
        if self.head.next is None:
            return None
        front = self.head.next
        self.head.next = front.next
        front.next = None
        return front.val
            

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #Criar a LinkedList
        linked_list = LinkedList()

        #Adicionar os valores a LinkedList
        for s in students:
            linked_list.add(val=s)

        i = 0                      # sanduíche do topo da pilha
        restantes = len(students)
        rejeicoes_seguidas = 0

        while restantes > 0 and rejeicoes_seguidas < restantes:
            valor = linked_list.remove_front()      # tira o da frente

            if valor == sandwiches[i]:              # ele quer o sanduíche?
                i += 1                              # próximo sanduíche
                restantes -= 1                      # ele saiu de vez
                rejeicoes_seguidas = 0              # alguém pegou, zera
            else:
                linked_list.add(valor)              # devolve pro fim da fila
                rejeicoes_seguidas += 1

        return restantes

        


            
        
