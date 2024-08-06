function carregar(){
    var msg = document.getElementById('msg');
    var img = document.getElementById('imagem');
    var data = new Date();
    var hora = data.getHours();
    msg.innerHTML = `Agora são ${hora} horas.`;

    if (hora >= 0 && hora < 12) {
        // Bom dia
        img.src = 'img/fotomanha.jpg';
        document.body.style.background = 'cyan';
    } else if (hora >= 12 && hora < 18) {
        // Boa tarde
        img.src = 'img/fototarde.jpg';
        document.body.style.background = 'orange';
    } else {
        // Boa noite
        img.src = 'img/fotonoite.jpg';
        document.body.style.background = 'black';
        
    }
}