class MPNeuron:
    def __init__(self):
        self.n = 3
        self.inputs = [1,1,1]
        self.weights = [1,1,1]
        self.threshold = 2.5

    def MP_Neuron_Input(self,n,inputs,weights,threshold):
        self.n = n
        self.inputs = inputs
        self.weights = weights
        self.threshold = threshold
    
    def MP_Neuron_Evaluate(self):
        '''print(self.inputs)
        print(self.weights)
        print(self.threshold)'''
        final_value = self.inputs[0]*self.weights[0] + self.inputs[1]*self.weights[1] + self.inputs[2]*self.weights[2]
        if(final_value < self.threshold):
            return 0
        else: return 1


NAND_gate_inputs = []

for i in range(3):
    NAND_gate_inputs.append(int(input(f"Enter {i+1} NAND GATE INPUT : ")))
print(NAND_gate_inputs)
n = 3
NAND_gate_weights = [-1,-1,-1]
NAND_gate_bias = -2
neurons = MPNeuron()



neurons.MP_Neuron_Input(n,NAND_gate_inputs,NAND_gate_weights,NAND_gate_bias)
print(neurons.MP_Neuron_Evaluate())



