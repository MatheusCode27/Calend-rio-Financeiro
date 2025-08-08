from fpdf import FPDF

# Criando o conteúdo do PDF
titulo = "Planejamento Financeiro - Agosto e Setembro"
conteudo = """
Resumo Geral por Etapas

Total acumulado até o dia 5 de setembro: R$ 805,00

Dia 15 de agosto
Receita:
- PIS: R$ 1.518,00
Despesas:
- Cartões Luiza + Itaú: R$ 774,00
- PIX para esposa (parcela carro): R$ 343,00
- PIX para esposa (cartão dela): R$ 100,00
- Cartão Nubank (vence dia 20): R$ 123,00
- Ônibus faculdade: R$ 40,00
Sobra guardada para o dia 5: R$ 138,00

Dia 20 de agosto
Receita:
- R$ 667,00
Destino:
- Guardado para pagar a faculdade
Dia 5 de setembro
Paga faculdade: R$ 612,00
Sobra: R$ 193,00
Receita do 5º dia útil de setembro: R$ 817,00
Total disponível: R$ 1.010,00

Pagamentos no dia 5 de setembro:
- Cartão atrasado (venc. 23 de agosto): R$ 710,00
- Cartão da mãe: R$ 296,00
Sobra final: R$ 4,00
"""

from datetime import date

# Dia 15 de agosto
receita_15 = 1518.00
despesas_15 = {
    "Cartões Luiza + Itaú": 774.00,
    "PIX esposa (carro)": 343.00,
    "PIX esposa (cartão)": 100.00,
    "Cartão Nubank": 123.00,
    "Ônibus faculdade": 40.00
}
sobra_15 = receita_15 - sum(despesas_15.values())  # Deve ser R$ 138,00

# Dia 20 de agosto
receita_20 = 667.00
guardado_faculdade = receita_20  # R$ 667,00 guardado

# Dia 5 de setembro
paga_faculdade = 612.00
sobra_faculdade = guardado_faculdade - paga_faculdade  # R$ 55,00
sobra_total_5_set = sobra_15 + sobra_faculdade  # R$ 193,00

receita_5_set = 817.00
total_disponivel = sobra_total_5_set + receita_5_set  # R$ 1.010,00

pagamentos_5_set = {
    "Cartão atrasado": 710.00,
    "Cartão da mãe": 296.00
}
sobra_final = total_disponivel - sum(pagamentos_5_set.values())  # R$ 4,00

# Exibir resumo
print("Resumo Financeiro:")
print(f"Sobra dia 15/08: R$ {sobra_15:.2f}")
print(f"Sobra após pagar faculdade: R$ {sobra_faculdade:.2f}")
print(f"Total disponível dia 05/09: R$ {total_disponivel:.2f}")
print(f"Sobra final após pagamentos: R$ {sobra_final:.2f}")



from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, "Resumo Financeiro - Agosto e Setembro", ln=True, align='C')
        self.ln(5)

    def section_title(self, title):
        self.set_font("Arial", 'B', 12)
        self.set_text_color(0, 0, 128)
        self.cell(0, 10, title, ln=True)
        self.set_text_color(0, 0, 0)

    def add_table(self, items):
        self.set_font("Arial", size=11)
        for label, value in items.items():
            self.cell(140, 8, label, border=0)
            self.cell(40, 8, f"R$ {value:.2f}", border=0, ln=True)
        self.ln(3)

# Dados
despesas_15 = {
    "Cartões Luiza + Itaú": 774.00,
    "PIX esposa (carro)": 343.00,
    "PIX esposa (cartão)": 100.00,
    "Cartão Nubank": 123.00,
    "Ônibus faculdade": 40.00
}
receita_15 = 1518.00
sobra_15 = receita_15 - sum(despesas_15.values())

receita_20 = 667.00
paga_faculdade = 612.00
sobra_faculdade = receita_20 - paga_faculdade
sobra_total_5_set = sobra_15 + sobra_faculdade

receita_5_set = 817.00
total_disponivel = sobra_total_5_set + receita_5_set

pagamentos_5_set = {
    "Cartão atrasado": 710.00,
    "Cartão da mãe": 296.00
}
sobra_final = total_disponivel - sum(pagamentos_5_set.values())

# Criar PDF
pdf = PDF()
pdf.add_page()

# Dia 15 de agosto
pdf.section_title("Dia 15 de Agosto")
pdf.cell(0, 8, f"Receita: R$ {receita_15:.2f}", ln=True)
pdf.cell(0, 8, "Despesas:", ln=True)
pdf.add_table(despesas_15)
pdf.cell(0, 8, f"Sobra guardada: R$ {sobra_15:.2f}", ln=True)
pdf.ln(5)

# Dia 20 de agosto
pdf.section_title("Dia 20 de Agosto")
pdf.cell(0, 8, f"Receita: R$ {receita_20:.2f}", ln=True)
pdf.cell(0, 8, f"Guardado para faculdade: R$ {receita_20:.2f}", ln=True)
pdf.ln(5)

# Dia 5 de setembro
pdf.section_title("Dia 5 de Setembro")
pdf.cell(0, 8, f"Pagamento faculdade: R$ {paga_faculdade:.2f}", ln=True)
pdf.cell(0, 8, f"Sobra após faculdade: R$ {sobra_faculdade:.2f}", ln=True)
pdf.cell(0, 8, f"Receita do dia: R$ {receita_5_set:.2f}", ln=True)
pdf.cell(0, 8, f"Total disponível: R$ {total_disponivel:.2f}", ln=True)
pdf.cell(0, 8, "Pagamentos:", ln=True)
pdf.add_table(pagamentos_5_set)
pdf.cell(0, 10, f"Sobra final: R$ {sobra_final:.2f}", ln=True)

# Salvar
pdf.output("controle_financeiro_visual.pdf")
