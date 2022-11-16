{
	const selector = document.querySelectorAll(".items");
	const checked = document.querySelectorAll(".checked");

	for (let index = 0; index < selector.length; index++) {
		const element = selector[index];
		element.addEventListener("click", () => {
			checked[index].classList.remove("visually-hidden");
		});
	}
}