from adding_alternatives_gui import AddingAlternativesGui


def main():
    features_names = ["salary", "qualifications", "travel_cost",
                      "benefits", "development_opportunities"]

    AddingAlternativesGui(features_names).run()


if __name__ == '__main__':
    main()
