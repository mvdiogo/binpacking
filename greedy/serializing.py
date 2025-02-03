import time

def binpack(peso, capacidade, inicio):
    # Sort weights in descending order (Best Fit Decreasing strategy)
    sorted_weights = sorted(peso, reverse=True)
    
    # Initialize lists:
    # 'bins' holds the current total weight in each bin,
    # 'bin_contents' holds the list of weights in each bin,
    # 'free_spaces' caches remaining capacity in each bin.
    bins = []
    bin_contents = []
    free_spaces = []
    
    # Process each weight from largest to smallest.
    for w in sorted_weights:
        # Use a list comprehension to find indices of bins that can hold 'w'
        candidates = [(i, free_spaces[i]) for i in range(len(free_spaces)) if free_spaces[i] >= w]
        
        if candidates:
            # Choose the candidate that minimizes wasted space (free_space - w)
            best_i, _ = min(candidates, key=lambda x: x[1] - w)
            bins[best_i] += w
            bin_contents[best_i].append(w)
            free_spaces[best_i] -= w  # update cached free space
        else:
            # No bin can accommodate 'w', so open a new bin.
            bins.append(w)
            bin_contents.append([w])
            free_spaces.append(capacidade - w)
    
    fim = time.time()
    print("Tamanho bolsa Best Fit= {}".format(len(bins)))
    print("Teto minimo= {}".format(len(bins)))
    print("Tempo total em segundos= {:.6f}".format(fim - inicio))
    
    # Return a tuple similar to your original function's structure.
    return len(bins), bins, bin_contents, bins, bin_contents

# Example usage:
if __name__ == "__main__":
    inicio = time.time()
    pesos = [10, 8, 5, 7, 6, 3, 2, 1, 4, 9]
    capacidade = 15
    result = binpack(pesos, capacidade, inicio)
