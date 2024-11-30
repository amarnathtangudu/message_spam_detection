# from message_information_extractor.url_extractor import extract_links
from message_information_extractor.url_extractor import parseText

# message = "Hey! Check out these links: https://example.com and www.anotherexample.org for more info."
# links = extract_links(message)
# print("Links found:", links)

# List of test messages with expected outputs
test_messages = [
    {
        "message": "Visit our main site at https://www.example.com, the subdomain at https://blog.example.com, and our backup site at http://backup.example.com.",
        "expected": ["https://www.example.com", "https://blog.example.com", "http://backup.example.com"]
    },
    {
        "message": "Check the latest updates at https://example.com/update?id=123&lang=en#section and also see our FAQ at https://faq.example.com?topic=networking.",
        "expected": ["https://example.com/update?id=123&lang=en#section", "https://faq.example.com?topic=networking"]
    },
    {
        "message": "For discounts, go to https://shop.example.com/deals?coupon=SUMMER%20SALE&ref=homepage or https://offers.example.com/discount#summer-sale.",
        "expected": ["https://shop.example.com/deals?coupon=SUMMER%20SALE&ref=homepage", "https://offers.example.com/discount#summer-sale"]
    },
    {
        "message": "Access the site via https://secure.example.com, the FTP server at ftp://ftp.example.com/files, and also consider visiting www.example.org for more info.",
        "expected": ["https://secure.example.com", "ftp://ftp.example.com/files", "www.example.org"]
    },
    {
        "message": "Connect to the dev environment at http://localhost:8080/api, or the production at https://example.com:443/home.",
        "expected": ["http://localhost:8080/api", "https://example.com:443/home"]
    },
    {
        "message": "See the documentation (https://docs.example.com/api/v1[version]) and the support page [https://support.example.com#contact].",
        "expected": ["https://docs.example.com/api/v1[version]", "https://support.example.com#contact"]
    },
    {
        "message": "Hello! This message contains no links, just text.",
        "expected": []
    },
    {
        "message": "Try example.com or www.example.com/test for more details.",
        "expected": ["www.example.com/test"]
    },
    {
        "message": "Access the document here: https://docs.example.com/file%20name%20with%20spaces.pdf",
        "expected": ["https://docs.example.com/file%20name%20with%20spaces.pdf"]
    },
    {
        "message": "Find us on social media at https://profile.social or on the tech site http://example.tech.",
        "expected": ["https://profile.social", "http://example.tech"]
    }
]

for i, test_case in enumerate(test_messages):
    message = test_case["message"]
    expected = test_case["expected"]
    result = parseText(message)
    print(f"Test Case {i+1}: {'Passed' if result == expected else 'Failed'}")
    print("Extracted Links:", result)
    print("Expected Links:", expected)
    print("---" * 10)
