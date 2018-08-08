$.ajax({
  url: 'https://randomuser.me/api/?results=100',
  dataType: 'json',
  success: function(data) {
    var people = data;
    // console.log(data);
    createCard(data);
  }
});

function createCard(data) {
    for (var i = 0; i<100; i++) {
        // console.log(data);
        var card= document.createElement('div');
        card.className = "card-item";
        var cards = document.querySelector(".cards");
        cards.appendChild(card);
        var header = document.createElement('div');
        header.className = "info-header";
        card.appendChild(header);
        var header_img = document.createElement('img');
        header_img.src = data.results[i].picture.medium;
        header.appendChild(header_img);
        var header_h1 = document.createElement('h1');
        header_h1.innerHTML = data.results[i].name.first + " " + data.results[i].name.last;
        header.appendChild(header_h1);
        var table = document.createElement('table');
        card.appendChild(table);
        var tr_1 = document.createElement('tr');
        table.appendChild(tr_1);
        var sexname = document.createElement('td');
        sexname.innerHTML = "Пол";
        tr_1.appendChild(sexname);
        var sexvalue = document.createElement('td');
        sexvalue.innerHTML = data.results[i].gender;
        tr_1.appendChild(sexvalue);
        var tr_2 = document.createElement('tr');
        table.appendChild(tr_2);
        var phonename = document.createElement('td');
        phonename.innerHTML = "Телефон";
        tr_2.appendChild(phonename);
        var phonevalue = document.createElement('td');
        phonevalue.innerHTML = data.results[i].phone;
        tr_2.appendChild(phonevalue);
        var tr_3 = document.createElement('tr');
        table.appendChild(tr_3);
        var emailname = document.createElement('td');
        emailname.innerHTML = "email";
        tr_3.appendChild(emailname);
        var emailvalue = document.createElement('td');
        emailvalue.innerHTML = data.results[i].email;
        tr_3.appendChild(emailvalue);
    }
}

