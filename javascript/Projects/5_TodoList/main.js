let add_task_btn = document.querySelector('button');
let task_content = document.querySelector('input');
let task_container = document.querySelector('.task-container');
let task, count=0, hr, target_element, new_task_content, para, task_to_delete, hr_to_delete;

add_task_btn.addEventListener('click', () => {
    count++;
    task = document.createElement('div');
    task.setAttribute('class', 'task');
    task.innerHTML = `<p>${task_content.value}</p>
    <div class="edit-options">
        <i class="fa-solid fa-edit task-option-icons edit-icon"></i>
        <i class="fa-solid fa-check task-option-icons check-icon"></i>
        <i class="fa-solid fa-trash task-option-icons trash-icon"></i>
    </div>`;
    task_content.value = "";
    if (count > 1){
        hr = document.createElement('hr');
        hr.setAttribute('class', 'separator');
        task_container.appendChild(hr);
    }
    task_container.appendChild(task);
    task_container.classList.add('show-task-container');
})

window.addEventListener('click', (e) => {
    target_element = e.target;
    if (target_element.classList.contains('edit-icon')){
        new_task_content = prompt("Enter new task:");
        // console.log(new_task_content);
        para = target_element.parentElement.previousElementSibling;
        // console.log(para);
        para.innerText = new_task_content;
    }
    if (target_element.classList.contains('check-icon')){
        para = target_element.parentElement.previousElementSibling;
        para.style.textDecoration = 'line-through';
    }
    if (target_element.classList.contains('trash-icon')){
        count--;
        task_to_delete = target_element.parentElement.parentElement;
        hr_to_delete = task_to_delete.previousElementSibling;
        if (hr_to_delete != null){
            hr_to_delete.remove();
        }
        else{
            if (count > 0){
                hr_to_delete = task_to_delete.nextElementSibling;
                hr_to_delete.remove();
            }
        }
        task_to_delete.remove();
        if (count == 0){
            task_container.classList.remove('show-task-container');
        }
    }
})