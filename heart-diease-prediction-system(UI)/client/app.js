

function onClickedheartdieasestatus() {
  console.log("Estimate price button clicked");

  var age = document.getElementById("uiage");
  var sex = document.getElementById("uisex");
  var trestbps = document.getElementById("uitrestbps");
  var chol = document.getElementById("uichol");
  var thalach = document.getElementById("uithalach");
  var oldpeak = document.getElementById("uioldpeak");
  var ca = document.getElementById("uica");
  var restecg = document.getElementById("uirestecg");
  var thal = document.getElementById("uithal");




  console.log(age.value);
  console.log(sex.value);

   var url = "http://127.0.0.1:5000/heart_diease_prediction"; //  Use this if you are NOT using nginx which is first 7 tutorials
   // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards


  $.post(url, {
      age: parseInt(age.value),
      sex: parseInt(sex.value),
      trestbps:   parseInt(trestbps.value),
      chol :  parseInt(chol.value),
      thalach :  parseInt(thalach.value),
      oldpeak :  parseFloat(oldpeak.value),
      ca :  parseInt(ca.value),
      restecg :  parseInt(restecg.value),
      thal :  parseInt(thal.value)



  },function(data, status) {

  console.log(data);
  console.log(status);

  if (data.heart_diease_status == 1) {
      estPrice.innerHTML = "<h2> patient has highest risk to develop the heart disease  </h2>";
      console.log(data.heart_diease_status.toString());

} else {
  estPrice.innerHTML = "<h2> patient has not risk to develop the heart disease  </h2>";
  console.log(data.heart_diease_status.toString());

}

  });
}


function onPageLoad() {
  console.log( "document loaded" );

	 var url1 = "http://127.0.0.1:5000/get_restecg_names"; // Use this if you are NOT using nginx which is first 7 tutorials
	 var url2 = "http://127.0.0.1:5000/get_thal_names"; // Use this if you are NOT using nginx which is first 7 tutorials

   //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url1,function(data, status) {
      console.log("got response for get_restecg_names request");
      if(data) {
          var restecg = data.restecg;
          var uirestecg = document.getElementById("restecg");
          $('#uirestecg').empty();
          for(var i in restecg) {
              var opt = new Option(restecg[i]);
              $('#uirestecg').append(opt);
          }
      }
  });

    $.get(url2,function(data, status) {
      console.log("got response for get_thal_names request");
      if(data) {
          var thal = data.thal;
          var uithal = document.getElementById("thal");
          $('#uithal').empty();
          for(var i in thal) {
              var opt = new Option(thal[i]);
              $('#uithal').append(opt);
          }
      }
  });

}

window.onload = onPageLoad;