document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('assignment-form');
    const nameInput = document.getElementById('assignment-name');
    const gradeInput = document.getElementById('assignment-grade');
    const assignmentsList = document.getElementById('assignments-list');
    const gpaDisplay = document.getElementById('gpa');

    let assignments = [];

    // Load from localStorage if available
    if (localStorage.getItem('assignments')) {
        assignments = JSON.parse(localStorage.getItem('assignments'));
        renderAssignments();
        updateGPA();
    }

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = nameInput.value.trim();
        const grade = parseFloat(gradeInput.value);

        if (name && !isNaN(grade) && grade >= 0 && grade <= 5) {
            assignments.push({ name, grade });
            saveAssignments();
            renderAssignments();
            updateGPA();
            form.reset();
            nameInput.focus();
        }
    });

    function renderAssignments() {
        assignmentsList.innerHTML = '';
        assignments.forEach(({ name, grade }, index) => {
            const li = document.createElement('li');
            li.textContent = `${name}: ${grade.toFixed(2)}`;

            // Create remove button
            const removeBtn = document.createElement('button');
            removeBtn.textContent = 'Remove';
            removeBtn.style.marginLeft = '10px';
            removeBtn.style.backgroundColor = '#e74c3c';
            removeBtn.style.color = 'white';
            removeBtn.style.border = 'none';
            removeBtn.style.borderRadius = '4px';
            removeBtn.style.cursor = 'pointer';
            removeBtn.style.padding = '2px 6px';
            removeBtn.style.fontSize = '0.8rem';

            removeBtn.addEventListener('click', () => {
                assignments.splice(index, 1);
                saveAssignments();
                renderAssignments();
                updateGPA();
            });

            li.appendChild(removeBtn);
            assignmentsList.appendChild(li);
        });
    }

    function updateGPA() {
        if (assignments.length === 0) {
            gpaDisplay.textContent = '0.00';
            return;
        }
        const total = assignments.reduce((sum, a) => sum + a.grade, 0);
        const gpa = total / assignments.length;
        gpaDisplay.textContent = gpa.toFixed(2);
    }

    function saveAssignments() {
        localStorage.setItem('assignments', JSON.stringify(assignments));
    }

    // Log all data to console on pressing "S"
    document.addEventListener('keydown', (e) => {
        if (e.key.toLowerCase() === 's') {
            console.log('Assignments:', assignments);
        }
        // Refresh the app on pressing "R"
        if (e.key.toLowerCase() === 'r') {
            window.location.reload();
        }
    });
});
