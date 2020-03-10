
function main() {
	let comments = document.getElementsByClassName('XQXOT')[0]
	comments = comments.children
	for (item of comments) {
		if (item.tagName == 'UL') {
			let svgs = item.getElementsByTagName('svg');
			for (svg of svgs) {
				if (svg.getAttribute('aria-label') === 'Like') {
					svg.parentNode.click()
					break
				}
			}	
		}
	}
}

