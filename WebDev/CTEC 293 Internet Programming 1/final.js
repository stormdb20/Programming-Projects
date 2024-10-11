
function loancalc(){
// Calculate loan amount
    const loaninfo = document.getElementById('loan-info');
    loaninfo.addEventListener('submit', function (event) {
        event.preventDefault();

    // Get user inputted values
        const coursenum = parseFloat(document.getElementById('coursenums').value);
        const courseprice = parseFloat(document.getElementById('courseprices').value);
        const loan = coursenum * courseprice;

    //Display output
        document.getElementById('cnum').innerHTML = 
        "Courses Taken: " + coursenum;

        document.getElementById('cprice').innerHTML = 
        "Course Price: $" + courseprice;

        document.getElementById('lamt').innerHTML = 
        "Loan Total: $" + loan;


});
}

function repaycalc(){
    // Student Loan Repayment Calculator
    const repaymentinfo = document.getElementById('repayment');
    repaymentinfo.addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent form submission

      // Retrieve input values
      const loanamt = parseFloat(document.getElementById('loanamts').value);
      const intrate = parseFloat(document.getElementById('intrates').value);
      const loandut = parseFloat(document.getElementById('loanterms').value);

      // Calculate loan repayment
      const monintrate = intrate / 100 / 12;
      const numpay = loandut * 12;

      const monpay = (loanamt * ((monintrate * Math.pow(1 + monintrate,numpay)) / (Math.pow(1 + monintrate,numpay) - 1)));
      const paytot = monpay * numpay;
      const inttot = paytot - loanamt;

      // Display the results
      document.getElementById('lamt2').innerHTML = 
        "Loan Amount: $" + loanamt;
        document.getElementById('irate').innerHTML = 
        "Interest Rate: " + intrate + "%";
        document.getElementById('lterm').innerHTML = 
        "Loan Term: " + loandut + " years";
        document.getElementById('mpa').innerHTML = 
        "Monthly Payment Amount: $" + monpay.toFixed(2);
        document.getElementById('totint').innerHTML = 
        "Total Interest: $" + inttot.toFixed(2);
        document.getElementById('totpay').innerHTML = 
        "Total Payment: $" + paytot.toFixed(2);
      
      
    });
}