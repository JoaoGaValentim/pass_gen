import random


def reverse(m_list) -> list:
    return m_list[::-1]


def remove_spaces(string) -> str:
    str_no_space = string.replace(" ", "")
    return str_no_space


def gen_pass(text) -> str:
    letters = [chr(i) for i in range(ord("a"), ord("z") + 1)]
    numbers = [i for i in range(10)]
    special = (
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        "-",
        "_",
        "+",
        "=",
        ".",
        "{",
        "}",
        "'",
        '"',
    )
    password = ""
    for l in text.lower():
        if not l.isdigit():
            letter_reverse = reverse(letters)[letters.index(l)] if l in letters else l
            password += random.choice(letters).upper() + letter_reverse

        if l.isdigit():
            password += (
                random.choice(letters).upper()
                + random.choice(special)
                + str(reverse(numbers)[numbers.index(int(l))])
            )

    return password


def add_account_pass(name_account, password):
    with open("password.txt", "a") as file:
        file.write("🙂 service: " + name_account + " 🔐 password: " + password + "\n")
    print("✅ Nova senha cadastrada com sucesso!")


def get_all_pass():
    with open("password.txt") as file:
        for data in file.readlines():
            print(data)


def app():
    loop = True
    while loop:
        try:
            print("=" * 10)
            print("1. Gerar senha para uma conta")
            print("2. Consultar senhas e contas")
            print("3. Sair")
            print("=" * 10)
            option = int(input("Número da opção selecionada >> "))

            if option == 1:
                account = input(
                    "Informe a senha de uma conta (ex.: Google, Facebook) >> "
                )
                password = remove_spaces(
                    gen_pass(input("🔐 Informe um texto para gerar a senha >> "))
                )

                add_account_pass(account, password)

            if option == 2:
                get_all_pass()

            if option == 3:
                loop = False

        except KeyboardInterrupt as e:
            print("Programa fechado pelo usuário")
            loop = False


if __name__ == "__main__":
    app()
