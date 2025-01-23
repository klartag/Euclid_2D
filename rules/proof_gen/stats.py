from matplotlib import pyplot as plt
import glob
from tqdm import tqdm

def main():
    proof_lengths = []
    proof_lengths_0 = []

    paths = glob.glob(r'C:\Users\v-ronsolan\Documents\euclid_data_out\samples_0_1\*.proof.txt')
    for path in tqdm(paths):
        text = open(path).read()
        statement_count = text.count('By')
        if path[-11] in '0123456789':
            proof_lengths.append(statement_count)

            if 'false' in text:
                print(f'False proof: {path}')

    bins = max(proof_lengths)
    plt.hist(proof_lengths, range=(0, bins), bins=bins)
    plt.hist(proof_lengths_0, range=(0, bins), bins=bins)
    plt.show()

if __name__ == '__main__':
    main()
