
// function formSwitch() {
//         lists= document.getElementsByName('event_type')
//         if (lists[1].checked) {
//             document.getElementById('event_text_title').style.display = "";
//             document.getElementById('workList').style.display = "";
//             document.getElementById('sportList').style.display = "none";
//             document.getElementById('foodList').style.display = "none";
//             document.getElementById('placeList').style.display = "none";
//
//         } else if (lists[2].checked) {
//             document.getElementById('event_text_title').style.display = "";
//             document.getElementById('workList').style.display = "none";
//             document.getElementById('sportList').style.display = "";
//             document.getElementById('e-sportList').style.display = "none";
//             document.getElementById('placeList').style.display = "none";
//
//         } else if (lists[3].checked) {
//             document.getElementById('event_text_title').style.display = "";
//             document.getElementById('workList').style.display = "none";
//             document.getElementById('sportList').style.display = "none";
//             document.getElementById('e-sportList').style.display = "";
//             document.getElementById('hobbyList').style.display = "none";
//
//         } else if (lists[4].checked) {
//             document.getElementById('event_text_title').style.display = "";
//             document.getElementById('workList').style.display = "none";
//             document.getElementById('sportList').style.display = "none";
//             document.getElementById('e-sportList').style.display = "none";
//             document.getElementById('hobbyList').style.display = "";
//
//         } else {
//             document.getElementById('event_text_title').style.display = "none";
//             document.getElementById('workList').style.display = "none";
//             document.getElementById('sportList').style.display = "none";
//             document.getElementById('e-sportList').style.display = "none";
//             document.getElementById('hobbyList').style.display = "none";
//
//         }
//     }
//         window.addEventListener('load', formSwitch());
//

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