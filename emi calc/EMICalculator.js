function calculateEMI() {
  const obj = {
      principal: document.getElementById("principalAmount").value,
      rate: (document.getElementById("interestRate").value),
      months: document.getElementById("tenure").value
  };

  console.log(obj);

  function emi(loan) {
      let rate=((loan.rate/100)/12);
      let top = Math.pow((1 + rate), loan.months);
      let bottom = top - 1;
      let ratio = top / bottom;
      result = loan.principal * rate * (ratio);

      console.log(result);
      
      return result.toFixed(2);
  }
   

  document.getElementById("result").innerHTML = "EMI is Rs." + emi(obj);
  

  return false;
}
function clear(){
    document.getElementById("result").innerHTML = "";
}
