
function formSwitch() {
        lists= document.getElementsByName('event_type')
        if (lists[1].checked) {
            document.getElementById('event_text_title').style.display = "";
            document.getElementById('workList').style.display = "";
            document.getElementById('sportList').style.display = "none";
            document.getElementById('foodList').style.display = "none";
            document.getElementById('placeList').style.display = "none";

        } else if (lists[2].checked) {
            document.getElementById('event_text_title').style.display = "";
            document.getElementById('workList').style.display = "none";
            document.getElementById('sportList').style.display = "";
            document.getElementById('e-sportList').style.display = "none";
            document.getElementById('placeList').style.display = "none";

        } else if (lists[3].checked) {
            document.getElementById('event_text_title').style.display = "";
            document.getElementById('workList').style.display = "none";
            document.getElementById('sportList').style.display = "none";
            document.getElementById('e-sportList').style.display = "";
            document.getElementById('hobbyList').style.display = "none";

        } else if (lists[4].checked) {
            document.getElementById('event_text_title').style.display = "";
            document.getElementById('workList').style.display = "none";
            document.getElementById('sportList').style.display = "none";
            document.getElementById('e-sportList').style.display = "none";
            document.getElementById('hobbyList').style.display = "";

        } else {
            document.getElementById('event_text_title').style.display = "none";
            document.getElementById('workList').style.display = "none";
            document.getElementById('sportList').style.display = "none";
            document.getElementById('e-sportList').style.display = "none";
            document.getElementById('hobbyList').style.display = "none";

        }
    }
        window.addEventListener('load', formSwitch());



