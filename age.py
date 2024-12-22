def main():
    try:
        user=int(input('Please enter your age(whole numbers please): '))
        print('You are',user,'years old!')
        if user%2==0:
            print('Your age is an even number!')
        else:
            print('Your age is an odd number!')
    except ValueError as x:
        print('WHY DID YOU NOT WRITE A WHOLE NUMBER!!! I TOLD YOU!\nI GOT THIS ERROR BECAUSE OF YOU:',x)
        main()
    except:
        print('THERE IS AN ERROR!!!')

main()