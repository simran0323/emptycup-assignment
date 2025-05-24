document.addEventListener('DOMContentLoaded', () => {
    // Store shortlisted items (using listing ID as the key)
    const shortlistedItems = new Set();

    // Get the shortlist filter toggle and listings container
    const shortlistFilter = document.getElementById('shortlist-filter');
    const listingsContainer = document.getElementById('listings-container');
    let isFilterActive = false;

    // Fetch listings data from the JSON file
    fetch('https://6831ee4cf4b0a3d1219a5626--wonderful-moxie-91af4a.netlify.app/')

        .then(response => response.json())
        .then(data => {
            // Render each listing
            data.forEach(listing => {
                const listingElement = document.createElement('section');
                listingElement.classList.add('listing');
                listingElement.setAttribute('data-id', listing.id);
                listingElement.innerHTML = `
                    <div class="listing-content">
                        <h2>${listing.name}</h2>
                        <div class="rating">
                            <img src="C:\Users\Simran Kumari\Desktop\EmptyCup\frontend\images\rating.png" alt="5 stars">
                        </div>
                        <p>${listing.description}</p>
                        <div class="stats">
                            <div class="stat">
                                <span class="value">${listing.projects}</span>
                                <span class="label">Projects</span>
                            </div>
                            <div class="stat">
                                <span class="value">${listing.years}</span>
                                <span class="label">Years</span>
                            </div>
                            <div class="stat">
                                <span class="value">${listing.price}</span>
                                <span class="label">Price</span>
                            </div>
                        </div>
                        <div class="contact">
                            ${listing.contact.map(phone => `<p>${phone}</p>`).join('')}
                        </div>
                    </div>
                    <div class="listing-actions">
                        <button>
                            Details <img src="C:\Users\Simran Kumari\Desktop\EmptyCup\frontend\images\detail.png" alt="Details">
                        </button>
                        <button>
                            Hide <img src="C:\Users\Simran Kumari\Desktop\EmptyCup\frontend\images\hide.png" alt="Hide">
                        </button>
                        <button class="shortlist-btn">
                            Shortlist <img src="C:\Users\Simran Kumari\Desktop\EmptyCup\frontend\images\shortlist.png" alt="Shortlist">
                        </button>
                        <button>
                            Report <img src="C:\Users\Simran Kumari\Desktop\EmptyCup\frontend\images\report.png" alt="Report">
                        </button>
                    </div>
                `;
                listingsContainer.appendChild(listingElement);
            });

            // Attach shortlist functionality to the dynamically created buttons
            const shortlistButtons = document.querySelectorAll('.shortlist-btn');
            shortlistButtons.forEach(button => {
                button.addEventListener('click', () => {
                    const listing = button.closest('.listing');
                    const listingId = parseInt.getAttribute('data-id');
                    const img = button.querySelector('img');

                    // Toggle shortlist state
                    if (shortlistedItems.has(listingId)) {
                        shortlistedItems.delete(listingId);
                        button.classList.remove('shortlisted');
                        img.src = 'images\shortlist.png';
                        img.alt = 'Shortlist';
                    } else {
                        shortlistedItems.add(listingId);
                        button.classList.add('shortlisted');
                        img.src = 'images\shortlisted.png';
                        img.alt = 'Shorlisted';
                    }

                    // Update visibility if filter is active
                    if (isFilterActive) {
                        updateListingVisibility();
                    }
                });
            });
        })
        .catch(error => console.error('Error fetching listings:', error));

    // Add click event to the shortlist filter
    shortlistFilter.addEventListener('click', () => {
        isFilterActive = !isFilterActive;
        shortlistFilter.classList.toggle('active', isFilterActive);
        updateListingVisibility();
    });

    // Function to update listing visibility based on filter
    function updateListingVisibility() {
        const listings = document.querySelectorAll('.listing');
        listings.forEach(listing => {
            const listingId = listing.getAttribute('data-id');
            if (isFilterActive) {
                listing.classList.toggle('hidden', !shortlistedItems.has(listingId));
            } else {
                listing.classList.remove('hidden');
            }
        });
    }
});