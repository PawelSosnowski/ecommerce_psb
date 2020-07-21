class Cart
{
  constructor(ownerID)
  {
    this.ownerID = ownerID;
    this.items = {};
  }

  addItem(itemID)
  {
    console.log(itemID);
    if(itemID in this.items)
      this.items[itemID] += 1;
    else
      this.items[itemID] = 1;

    console.log(this);
  }

};

let cart = new Cart(1);

var table = document.getElementById("product_table");
var tableHeader = table.appendChild(document.createElement("thead"));

var idProduktu = tableHeader.appendChild(document.createElement("th"));
idProduktu.innerHTML = "ID produktu";
var cena = tableHeader.appendChild(document.createElement("th"));
cena.innerHTML = "Cena";
var kategoria = tableHeader.appendChild(document.createElement("th"));
kategoria.innerHTML = "Kategoria";
var producent = tableHeader.appendChild(document.createElement("th"));
producent.innerHTML = "Producent";
var ilosc = tableHeader.appendChild(document.createElement("th"));
ilosc.innerHTML = "Ilosc";
var dodaj = tableHeader.appendChild(document.createElement("th"));
dodaj.innerHTML = "Dodaj do koszyka";

var tbody = table.appendChild(document.createElement("tbody"));
for(let i = 0; i < products.length; i++ )
{
  let row = tbody.appendChild(document.createElement("tr"));
  let fields = products[i]["fields"];
  let values = Object.values(fields);
  let idTD = row.appendChild(document.createElement("td"));
  let itemID = products[i]["pk"];
  idTD.innerHTML = itemID;

  for(let j = 0; j < values.length; j++)
  {
      let td = row.appendChild(document.createElement("td"));
      td.innerHTML = values[j];
  }

  let buttonTD = row.appendChild(document.createElement("td"));
  let button = buttonTD.appendChild(document.createElement("button"));
  button.innerHTML = "Dodaj";
  button.onclick = () => cart.addItem(itemID);
}
let button = document.getElementById("zamow");
