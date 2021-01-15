class MySort:
    @staticmethod
    def bubble(data):
        for i in range(1, len(data)):
            for j in range(0, len(data)-1):
                print()
                if data[i] > data[j+1]:
                    data[i], data[j+1] = data[j+1], data[i]

        return data

    @staticmethod
    def quick(data, low, high):
        def partition(low, higj):
            pivot = data[high]
            left = low
            
            for right in range(low, high):
                if data[right] < pivot:
                    data[left], data[right] = data[right], data[left]
                    left += 1
            data[left], data[right] = data[right], data[left]
            return left
        
        if low < high:
            pivot = partition(low, high)
            quick(data, low, pivot - 1)
            quick(data, pivot + 1, high)

        return data

    
