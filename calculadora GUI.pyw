import PySimpleGUI as pg
from math import pi
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')

pg.theme('Reddit')
layout = [
    [pg.Text('1 - Calcular Área \n2 - Calcular Volume \n3 - Função de Segundo Grau')],
    [pg.Text('Opção'), pg.Input(key='opção')],
    [pg.Button('Calcular')],
]
janela = pg.Window('Calculadora Geométrica', layout)

while True:
    eventos, valores = janela.read()
    if eventos == pg.WINDOW_CLOSED:
        break
    if eventos == 'Calcular':
        while True:
            if valores['opção'] == '1':
                while True:
                    layout2 = [
                        [pg.Text('• Triângulo\n• Retângulo\n• Quadrado\n• Círculo\n• Trapézio'), pg.Input(key='opção1')],
                        [pg.Button('Entrar')],
                    ]
                    janela2 = pg.Window('Python', layout2)
                    eventos2, valores2 = janela2.read()
                    janela2.close()
                    if eventos2 == pg.WINDOW_CLOSED:
                        break
                    if valores2['opção1'] == 'triangulo' or valores2['opção1'] == 'triângulo':
                        while True:
                            layout4 = [
                                [pg.Text('Digite o valor da base:'), pg.Input(key='b')],
                                [pg.Text('Digite o valor da altura:'), pg.Input(key='h')],
                                [pg.Button('Inserir')],
                            ]
                            janela4 = pg.Window('Python', layout4)
                            eventos4, valores4 = janela4.read()
                            janela4.close()
                            
                            if eventos4 == pg.WINDOW_CLOSED:
                                break
                            if eventos4 == 'Inserir':
                                intb = int(valores4['b'])
                                inth = int(valores4['h'])
                                       
                                areaTriangulo = (intb * inth) / 2
                            
                                layout5 = [
                                    [pg.Text(f'O valor da área é de {areaTriangulo} unidades.')],
                                ]
                                janela5 = pg.Window('Python', layout5)
                                eventos5, valores5 = janela5.read()
                            if eventos5 == pg.WINDOW_CLOSED:
                                break
                            
                    if valores2['opção1'] == 'retangulo' or valores2['opção1'] == 'retângulo':
                        while True:
                            layoutRet = [
                                [pg.Text('Digite o valor da base:'), pg.Input(key='b')],
                                [pg.Text('Digite o valor da altura:'), pg.Input(key='h')],
                                [pg.Button('Inserir')],
                            ]
                            janelaRet = pg.Window('Python', layoutRet)
                            eventosRet, valoresRet = janelaRet.read()
                            janelaRet.close()
                            
                            if eventosRet == pg.WINDOW_CLOSED:
                                break
                            if eventosRet == 'Inserir':
                                intb = int(valoresRet['b'])
                                inth = int(valoresRet['h'])
                                       
                                areaRetangulo = (intb * inth)
                            
                                layoutResRet = [
                                    [pg.Text(f'O valor da área é de {areaRetangulo} unidades.')],
                                ]
                                janelaResRet = pg.Window('Python', layoutResRet)
                                eventosResRet, valoresResRet = janelaResRet.read()
                            if eventosResRet == pg.WINDOW_CLOSED:
                                break

                    if valores2['opção1'] == 'quadrado':
                        while True:
                            pg.theme('Reddit')
                            layoutQuad = [
                                [pg.Text('Digite o valor do lado:'), pg.Input(key='l')],
                                [pg.Button('Inserir')],
                            ]
                            janelaQuad = pg.Window('Python', layoutQuad)
                            eventosQuad, valoresQuad = janelaQuad.read()
                            janelaQuad.close()
                            
                            if eventosQuad == pg.WINDOW_CLOSED:
                                break
                            if eventosQuad == 'Inserir':
                                intl = int(valoresQuad['l'])
                                       
                                areaQuadrado = (intl ** 2)
                            
                                layoutResQuad = [
                                    [pg.Text(f'O valor da área é de {areaQuadrado} unidades.')],
                                ]
                                janelaResQuad = pg.Window('Python', layoutResQuad)
                                eventosResQuad, valoresResQuad = janelaResQuad.read()
                            if eventosResQuad == pg.WINDOW_CLOSED:
                                break

                    if valores2['opção1'] == 'círculo' or valores2['opção1'] == 'circulo':
                        while True:
                            layoutCir = [
                                [pg.Text('Digite o valor do raio:'), pg.Input(key='r')],
                                [pg.Button('Inserir')],
                            ]
                            janelaCir = pg.Window('Python', layoutCir)
                            eventosCir, valoresCir = janelaCir.read()
                            janelaCir.close()
                            
                            if eventosCir == pg.WINDOW_CLOSED:
                                break
                            if eventosCir == 'Inserir':
                                intr = int(valoresCir['r'])
                                       
                                areaCirculo = pi * (intr ** 2)
                            
                                layoutResCir = [
                                    [pg.Text('O valor da área é de {:.3f} unidades.' .format(areaCirculo))],
                                ]
                                janelaResCir = pg.Window('Python', layoutResCir)
                                eventosResCir, valoresResCir = janelaResCir.read()
                            if eventosResCir == pg.WINDOW_CLOSED:
                                break

                    if valores2['opção1'] == 'trapézio' or valores2['opção1'] == 'trapezio':
                        while True:
                            layoutTra = [
                                [pg.Text('Digite o valor da base maior: '), pg.Input(key='B')],
                                [pg.Text('Digite o valor da base menor:'), pg.Input(key='b')],
                                [pg.Text('Digite o valor da altura:         '), pg.Input(key='h')],
                                [pg.Button('Inserir')],
                            ]
                            janelaTra = pg.Window('Python', layoutTra)
                            eventosTra, valoresTra = janelaTra.read()
                            janelaTra.close()
                            
                            if eventosTra == pg.WINDOW_CLOSED:
                                break
                            if eventosTra == 'Inserir':
                                intB = int(valoresTra['B'])
                                intb = int(valoresTra['b'])
                                inth = int(valoresTra['h'])
                                       
                                areaTrapezio = ((intB + intb) * inth) / 2
                            
                                layoutResTra = [
                                    [pg.Text('O valor da área é de {:.3f} unidades.' .format(areaTrapezio))],
                                ]
                                janelaResTra = pg.Window('Python', layoutResTra)
                                eventosResTra, valoresResTra = janelaResTra.read()
                            if eventosResTra == pg.WINDOW_CLOSED:
                                break
                                        

                if eventos2 == pg.WINDOW_CLOSED:
                    break
            if valores['opção'] == '2':
                layout3 = [
                    [pg.Text('• Cubo\n• Paralelepípedo\n• Cilindro\n• Esfera'), pg.Input(key='opção2')],
                    [pg.Button('Entrar')],
                ]
                janela3 = pg.Window('Python', layout3)
                eventos3, valores3 = janela3.read()
                
                if eventos3 == pg.WINDOW_CLOSED:
                    break

            if valores['opção'] == '3':
                while True:
                    layoutop3 = [
                        [pg.Text('Digite o valor de a:'), pg.Input(key='a')],
                        [pg.Text('Digite o valor de b:'), pg.Input(key='b')],
                        [pg.Text('Digite o valor de c:'), pg.Input(key='c')],
                        [pg.Button('Calcular')],
                    ]
                    janelaop3 = pg.Window('Python', layoutop3)
                    eventosop3, valoresop3 = janelaop3.read()
                    janelaop3.close()
                    
                    if eventosop3 == pg.WINDOW_CLOSED:
                        break
                    
                    if eventosop3 == 'Calcular':
                        inta = int(valoresop3['a'])
                        intb = int(valoresop3['b'])
                        intc = int(valoresop3['c'])
                        delta = (intb ** 2) - 4 * inta *intc 
                        x1 = (-intb  + sqrt(delta)) / 2 * inta
                        x2 = (-intb - sqrt(delta)) / 2 * inta

                        layoutResOp3 = [
                            [pg.Text(f'O delta é {delta} e os valores de x são {x1} e {x2}.')],
                            [pg.Button('Visualizar gráfico')],
                        ]
                        janelaResOp3 = pg.Window('Python', layoutResOp3)
                        eventosResOp3, valoresResOp3 = janelaResOp3.read()
                        janelaResOp3.close()
                        
                        if eventosResOp3 == pg.WINDOW_CLOSED:
                            break

                        if eventosResOp3 == 'Visualizar gráfico':
                            x=[]
                            y=[]
                            valorY = -15
                            valorX = -15
                            while valorX <= 15:
                                valorY = (inta * valorX ** 2) + (intb * valorX) + (intc)
                                y.append(valorY)
                                x.append(valorX)
                                valorX = valorX + 0.5
                            fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
                            fig.add_subplot(111).plot(x,y)

                            def draw_figure(canvas, figure):
                                figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
                                figure_canvas_agg.draw()
                                figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
                                return figure_canvas_agg

                            layoutGraf = [[pg.Text('Gráfico:')],
                                [pg.Canvas(key='-CANVAS-')],
                                [pg.Button('Ok')]]

                            windowGraf = pg.Window('Gráfico da Função', layoutGraf, finalize=True, element_justification='center')
                            fig_canvas_agg = draw_figure(windowGraf['-CANVAS-'].TKCanvas, fig)
                            eventosGraf, valuesGraf = windowGraf.read()
                            windowGraf.close()

                            if eventosGraf in (pg.WINDOW_CLOSED, 'Ok'):
                                break
         
                        if eventosResOp3 == pg.WINDOW_CLOSED:
                            break
                            
                if eventosop3 == pg.WINDOW_CLOSED:
                    break

                    
            if eventos == pg.WINDOW_CLOSED:
                break
