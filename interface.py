import customtkinter

class App(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()

        #window title, size
        self.title("elderlyARCognitiveApplication")
        self.geometry("1900x1040+0+0")


if __name__ == "__main__":
    inter = App()
    inter.mainloop()