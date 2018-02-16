"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

text_sample = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec non nisl ultricies, scelerisque mi ac, vestibulum neque. Ut ullamcorper rhoncus."

TESTS = {
    "Basics": [
        {
            "input": [text_sample, 20],
            "answer": '''Lorem ipsum dolor
sit amet,
consectetur
adipiscing elit.
Donec non nisl
ultricies,
scelerisque mi ac,
vestibulum neque. Ut
ullamcorper rhoncus.'''
        },
        {
            "input": [text_sample, 10],
            "answer": '''Lorem
ipsum
dolor sit
amet,
consectetur
adipiscing
elit.
Donec non
nisl
ultricies,
scelerisque
mi ac,
vestibulum
neque. Ut
ullamcorper
rhoncus.'''
        }
    ],
    "Extra": [
        {
            "input": ["Lorem ipsum", 20],
            "answer": "Lorem ipsum"
        }
    ]
}
