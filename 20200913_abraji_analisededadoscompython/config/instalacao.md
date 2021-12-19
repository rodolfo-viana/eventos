## Instalação

### Passo a passo

> Caso prefira fazer o download do vídeo que mostra como fazer a instalação no Windows, [clique aqui](https://github.com/rodolfo-viana/eventos/raw/main/abraji_20200913/config/como_instalar.mp4).

Python não vem "de fábrica" com Windows, e se você é usuário de MacOS ou Linux, possivelmente tem a versão 2.7 na sua máquina —versão obsoleta.

Para instalar o Python 3, siga este passo a passo:

- Vá à página oficial de download de Python [[link](https://www.python.org/downloads/)]
- Faça o download da versão mais recente para seu sistema operacional (Windows, MacOS, Linux)
- Clique no arquivo para começar a instalação
- Durante a instalação, certifique-se de clicar nas opções _Install launcher for all users (recommended)_ e _Add Python x.x to PATH_
- Clique no botão _Install Now_
- Se e quando aparecer a mensagem _Do you want the allow the following program to make changes to this computer?_, escolha _Yes_
- Uma janela de instalação irá aparecer. Quando a barra de progresso chegar ao fim, a instalação estará completa
- Para checar se a instalação correu perfeitamente, vá ao console (aplicativo _Terminal_ no MacOS e Linux, e _Prompt de Comando_ no Windows) e digite `python --version` ou `python3 --version`, caso seu sistema seja MacOS ou Linux. Depois de pressionar Enter, você terá uma mensagem com a versão de Python que instalou —por exemplo, `Python 3.8.5`. Isso significa que a instalação foi concluída com êxito

Além de Python, vamos usar bibliotecas externas. São elas `Pandas` (para lidar com dados de forma tabulada) e `Matplotlib` (para gerar gráficos). Também vamos usar `Jupyter Notebook`, que é um editor onde escreveremos os códigos.

Para instalar tudo isso, siga este passo a passo depois de ter Python 3 na sua máquina:

- Abra o console (aplicativo _Terminal_ no MacOS e Linux, e _Prompt de Comando_ no Windows)
- Digite `python -m pip install jupyter pandas matplotlib` ou `python3 -m pip install jupyter pandas matplotlib`, dependendo do seu sistema operacional
- Aguarde o processo de instalação chegar ao fim
- Para checar se tudo foi instalado adequadamente, digite `jupyter notebook`. Uma tela do navegador irá abrir, assegurando que `Jupyter Notebook` foi instalado com êxito
- No canto superior direito, escolha _New_ > _Python 3_
- Quando abrir a tela em branco, copie e cole essas linhas:

```py
import pandas
import matplotlib.pyplot
```

- Pressione o botão de _play_ na barra de tarefas, na parte superior da tela
- Se aparecer apenas uma linha em branco e nenhum erro, isso significa que `Pandas` e `Matplotlib` foram instalados com sucesso
