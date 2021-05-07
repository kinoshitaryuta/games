function imgPreView(event) {
  let file = event.target.files[0];
  let reader = new FileReader();
  let preview = document.getElementById("preview");
  let previewImage = document.getElementById("previewImage");


  if(previewImage != null) {
    preview.removeChild(previewImage);
  }
  reader.onload = function(event) {
    let img = document.createElement("img");
    img.setAttribute("src", reader.result);
    img.setAttribute("id", "previewImage");
    preview.appendChild(img);
  };

  reader.readAsDataURL(file);

}
window.onload = function (){
	var today = new Date();
	today.setDate(today.getDate());
	var yyyy = today.getFullYear();
	var mm = ("0"+(today.getMonth()+1)).slice(-2);
	var dd = ("0"+today.getDate()).slice(-2);
	document.getElementById("date").value = yyyy + '-' + mm + '-' + dd;
}



const targetMain = document.getElementById('click_out_main');
const clicksMain = document.getElementById('clicks_main');

clicksMain.addEventListener('click', () => {
  targetMain.style.display = "none";
}, false);