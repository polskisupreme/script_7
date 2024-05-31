import re


def parse_cigar(cigar_string):
    # Znajdź wszystkie segmenty z 'M' w CIGAR, które oznaczają dopasowania
    matches = re.finditer(r'(\d+)M', cigar_string)
    longest_match_length = 0
    longest_match_position = 0
    current_position = 0

    for match in matches:
        length = int(match.group(1))
        if length > longest_match_length:
            longest_match_length = length
            longest_match_position = current_position
        current_position += length

    return longest_match_length, longest_match_position


def main():
    file_path = 'my_alignment.txt'

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('query'):
                parts = line.strip().split()
                cigar_string = parts[5]  # Zakładamy, że notacja CIGAR jest w szóstym polu
                max_length, max_position = parse_cigar(cigar_string)
                print(f"Maksymalna długość dopasowania: {max_length}")
                print(f"Maksymalna pozycja dopasowania: {max_position}")
                break


if __name__ == "__main__":
    main()
