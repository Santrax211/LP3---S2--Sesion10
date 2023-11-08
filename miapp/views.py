from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request,"index.html")

def saludo(request):
    return render(request,"saludo.html")

def rango(request):
    a = 10
    b = 20
    resultado = f"""
        <h2>Numeros de [{a},{b}]</h2>
        Resultado: <br>
        <ul>
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a += 1
    resultado += "</ul>"
    return HttpResponse(resultado)

layout = """
    <h1>Proyecto Web (LP3) | Flor Cerdán</h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio"> Inicio</a>
        </li>
        <li>
            <a href="/saludo">Mensaje de saludo</a>
        </li>
        <li>
            <a href="/rango">Mostrar Numeros [a,b]</a>
        </li>
        <li>
            <a href="/rango2/10/15">Mostrar búmeros [10,15]</a]>
        </li>
    </ul>
    </hr>
"""

def rango2(request,a=40,b=10):
    if a>b:
        return redirect("rango2",a=b,b=a)
    resultado = f"""
    <h2>Números de [{a},{b}]</h2>
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1
    resultado += "</ul>"
    
    return HttpResponse(layout+resultado)

     