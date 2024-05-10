function patientInfo(){
    var patientData =  JSON.parse(localStorage.getItem('patients')) || [];
    var loginEmail=localStorage.getItem('email');
    for(let i=0;i<patientData.length;i++){
        if(loginEmail===patientData[i]['email']){
            document.getElementById('name').innerHTML=patientData[i]['name'];
            document.getElementById('dof').innerHTML=patientData[i]['birthdaydate'];
            document.getElementById('address').innerHTML=patientData[i]['address'];
            document.getElementById('cn').innerHTML=patientData[i]['phone'];
            document.getElementById('appDate').innerHTML=patientData[i]['date1'];
            document.getElementById('appTime').innerHTML=patientData[i]['time1'];
            if(patientData[i]['primary1']==true){
                document.getElementById('services1').innerHTML='Primary Care'
            }
             if(patientData[i]['motherhood1']==true){
                document.getElementById('services2').innerHTML='Motherhood and childhood'
            }
             if(patientData[i]['lab1']==true){
                document.getElementById('services3').innerHTML='Laboratory Tests'
            }
             if(patientData[i]['dental1']==true){
                document.getElementById('services1').innerHTML='Dental Care'
            }
           
           
            
  
    }
    }
  
}
patientInfo();
// var info=document.getElementsByTagName('body')[0];
// console.log(info);
// info.addEventListener('load',function(e){
//     e.preventDefault();
//        var patientData =  JSON.parse(localStorage.getItem('patients')) || [];
//     var loginEmail=localStorage.getItem('email');
//     for(let i=0;i<patientData.length;i++){
//         if(loginEmail===patientData[i]['email']){
//             document.getElementById('name').innerHTML=patientData[i]['name'];
//              document.getElementById('dof').innerHTML=patientData[i]['birthdaydate'];
//               document.getElementById('address').innerHTML=patientData[i]['address'];
//                document.getElementById('cn').innerHTML=patientData[i]['phone'];
//     }
//     }
// })
