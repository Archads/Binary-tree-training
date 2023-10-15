class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value) #checando se ha uma node do aldo esquerdo
            else:
                self.left.insert(value) #caso ja tenha ir para o valor a baixo 
        else:
            if self.right is None:        #caso o valor seja maior colocar do lado direito essa parrte checa se tem como colocar la
                self.right  = TreeNode(value)
            else:
                self.right.insert(value)


    def travessia_ordenada(self): #ir o mais para a esquerda o possível
        if self.left:
            self.left.travessia_ordenada()