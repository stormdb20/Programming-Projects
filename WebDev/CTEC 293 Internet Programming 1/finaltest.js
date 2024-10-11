// Course Cost Calculator
function loancalc(){

    const courseCostForm = document.getElementById('course-cost-form');

courseCostForm.addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent form submission

  // Retrieve input values
  const numCourses = parseFloat(document.getElementById('num-courses').value);
  const costPerCourse = parseFloat(document.getElementById('cost-per-course').value);
  const totalCost = numCourses * costPerCourse;

  // Display the results
  document.getElementById('results').innerHTML = `
    <h2>Course Cost</h2>
    <p>Total Courses: ${numCourses}</p>
    <p>Cost per Course: $${costPerCourse}</p>
    <p>Total Cost: $${totalCost}</p>
  `;
});



}


function repaycalc(){

// Student Loan Repayment Calculator
const loanRepaymentForm = document.getElementById('loan-repayment-form');
loanRepaymentForm.addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent form submission

  // Retrieve input values
  const loanAmount = parseFloat(document.getElementById('loan-amount').value);
  const interestRate = parseFloat(document.getElementById('interest-rate').value);
  const loanTerm = parseFloat(document.getElementById('loan-term').value);

  // Calculate loan repayment
  const monthlyInterestRate = interestRate / 100 / 12;
  const numPayments = loanTerm * 12;

  const monthlyPayment = (loanAmount * monthlyInterestRate) / (1 - Math.pow(1 + monthlyInterestRate, -numPayments));
  const totalPayment = monthlyPayment * numPayments;
  const totalInterest = totalPayment - loanAmount;

  // Display the results
  document.getElementById('results').innerHTML += `
    <h2>Loan Repayment</h2>
    <p>Loan Amount: $${loanAmount}</p>
    <p>Interest Rate: ${interestRate}%</p>
    <p>Loan Term: ${loanTerm} years</p>
    <p>Monthly Payment: $${monthlyPayment.toFixed(2)}</p>
    <p>Total Payment: $${totalPayment.toFixed(2)}</p>
    <p>Total Interest: $${totalInterest.toFixed(2)}</p>
  `;
});
}