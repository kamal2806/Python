def main():
    game = ['Rock','Paper','Scissors','Lizard','Spock']
    print_list(game)

def print_list(o):
    for i in o:
        print(i,end=' ',flush=True)

if __name__ == '__main__' : main()