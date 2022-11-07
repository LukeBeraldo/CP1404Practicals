"""
CP1404/CP5632 Practical - Programming language
Expected time: 1 hour
Actual time: 45 mins
"""

from programming_language import ProgrammingLanguage


def main():
    """Practise class creation and display"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages = [python, ruby, visual_basic]

    dynamic_languages = [language for language in languages if language.is_dynamic()]
    print(f"The dynamically typed languages are:")
    for language in dynamic_languages:
        print(language.name)


main()
