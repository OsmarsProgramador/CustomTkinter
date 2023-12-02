import customtkinter

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("600x1000")

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
""" Configura a coluna de número 3 (contando a partir do zero) do widget app para ter um peso de 1.
    Ao configurar o peso de uma coluna, você está especificando como o espaço horizontal disponível
deve ser distribuído entre as colunas. Nesse caso, ao definir o peso como 1 para a coluna 3,
você está indicando que essa coluna deve receber uma parte igual do espaço disponível em relação
às outras colunas que também possuem um peso definido.
    Essa configuração é útil quando você deseja que as colunas se expandam ou contraiam de forma
proporcional quando a janela ou o widget pai for redimensionado. O peso determina a proporção em que
cada coluna receberá o espaço disponível. """
app.grid_columnconfigure(3, weight=1)

f1 = customtkinter.CTkFrame(app, fg_color="gray10", corner_radius=0)
f1.grid(row=0, column=0, rowspan=1, columnspan=1, sticky="nsew")
f1.grid_columnconfigure(0, weight=1)

f2 = customtkinter.CTkFrame(app, fg_color="gray10", corner_radius=0)
f2.grid(row=0, column=1, rowspan=1, columnspan=1, sticky="nsew")
f2.grid_columnconfigure(0, weight=1)

f3 = customtkinter.CTkFrame(app, fg_color="gray85", corner_radius=0)
""" configura o posicionamento e o dimensionamento do widget f3 dentro do seu widget pai.

O parâmetro row=0 define que o widget f3 será posicionado na primeira linha do seu widget pai.
O parâmetro column=2 define que o widget f3 será posicionado na terceira coluna do seu widget pai.
O parâmetro rowspan=1 define que o widget f3 ocupará apenas uma linha verticalmente.
O parâmetro columnspan=1 define que o widget f3 ocupará apenas uma coluna horizontalmente.
O parâmetro sticky="nsew" define como o widget f3 se comportará quando o widget pai for redimensionado.
"nsew" significa que o widget se expandirá nas direções norte, sul, leste e oeste, preenchendo todo o espaço disponível. """
f3.grid(row=0, column=2, rowspan=1, columnspan=1, sticky="nsew")
f3.grid_columnconfigure(0, weight=1)

f4 = customtkinter.CTkFrame(app, fg_color="gray90", corner_radius=0)
f4.grid(row=0, column=3, rowspan=1, columnspan=1, sticky="nsew")
f4.grid_columnconfigure(0, weight=1)

for i in range(0, 16, 1):
    b = customtkinter.CTkButton(f1, corner_radius=i, height=30, border_width=1, text=f"{i} {i-1}",
                                border_color="white", fg_color=None, text_color="white")
    # b = tkinter.Button(f1,  text=f"{i} {i-2}", width=20)
    b.grid(row=i, column=0, pady=5, padx=15, sticky="nsew")

    b = customtkinter.CTkButton(f2, corner_radius=i, height=30, border_width=0, text=f"{i}",
                                fg_color="#228da8")
    b.grid(row=i, column=0, pady=5, padx=15, sticky="nsew")

    b = customtkinter.CTkButton(f3, corner_radius=i, height=30, border_width=1, text=f"{i} {i-1}",
                                fg_color=None, border_color="gray20", text_color="black")
    b.grid(row=i, column=0, pady=5, padx=15, sticky="nsew")

    b = customtkinter.CTkButton(f4, corner_radius=i, height=30, border_width=0, text=f"{i}",
                                border_color="gray10", fg_color="#228da8")
    b.grid(row=i, column=0, pady=5, padx=15, sticky="nsew")

app.mainloop()
