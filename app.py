from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/jobs")
def jobs():
    # Mock job listings — replace with real data later
    jobs_data = [
        {
            "id": 1,
            "title": "Senior Real Estate Agent",
            "company": "Nestoria",
            "location": "Miami, Florida",
            "type": "Full-time",
            "type_class": "full",
            "experience": "3+ years",
            "salary": "$70k - $95k / yr",
            "description": "Lead high-value property sales and build lasting relationships with premium clients across South Florida.",
            "tags": ["Sales", "Negotiation", "CRM"],
            "posted": "2 days ago",
            "icon": "fa-handshake"
        },
        {
            "id": 2,
            "title": "Property Manager",
            "company": "Nestoria",
            "location": "Chicago, Illinois",
            "type": "Full-time",
            "type_class": "full",
            "experience": "2+ years",
            "salary": "$55k - $72k / yr",
            "description": "Oversee a portfolio of residential properties, coordinate maintenance, and ensure tenant satisfaction.",
            "tags": ["Operations", "Customer Service", "Property"],
            "posted": "5 days ago",
            "icon": "fa-building"
        },
        {
            "id": 3,
            "title": "Real Estate Photographer",
            "company": "Nestoria Studios",
            "location": "Austin, Texas",
            "type": "Contract",
            "type_class": "contract",
            "experience": "1+ years",
            "salary": "$45 - $80 / shoot",
            "description": "Capture stunning interior and exterior photography for our property listings across the Austin metro area.",
            "tags": ["Photography", "Editing", "Drone"],
            "posted": "1 week ago",
            "icon": "fa-camera"
        },
        {
            "id": 4,
            "title": "Mortgage Advisor",
            "company": "Nestoria Finance",
            "location": "New York, USA",
            "type": "Full-time",
            "type_class": "full",
            "experience": "4+ years",
            "salary": "$85k - $120k / yr",
            "description": "Guide clients through mortgage options, pre-approvals, and financing strategies for their new homes.",
            "tags": ["Finance", "Advisory", "Compliance"],
            "posted": "3 days ago",
            "icon": "fa-chart-line"
        },
        {
            "id": 5,
            "title": "Marketing Specialist",
            "company": "Nestoria",
            "location": "Remote",
            "type": "Remote",
            "type_class": "remote",
            "experience": "2+ years",
            "salary": "$50k - $68k / yr",
            "description": "Drive digital campaigns across social media, email, and search to attract new buyers and sellers.",
            "tags": ["SEO", "Ads", "Content"],
            "posted": "4 days ago",
            "icon": "fa-bullhorn"
        },
        {
            "id": 6,
            "title": "Frontend Engineer",
            "company": "Nestoria Tech",
            "location": "Remote",
            "type": "Remote",
            "type_class": "remote",
            "experience": "3+ years",
            "salary": "$90k - $130k / yr",
            "description": "Build and maintain the Nestoria property platform using modern HTML, CSS, JavaScript, and Jinja2.",
            "tags": ["HTML", "CSS", "JavaScript"],
            "posted": "Just now",
            "icon": "fa-code"
        }
    ]
    return render_template("jobs.html", jobs=jobs_data)


if __name__ == "__main__":
    app.run(debug=True)