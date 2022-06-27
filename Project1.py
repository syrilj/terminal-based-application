# A terminal-based application to lookup, proccess, and plot data based on given user input and provided csv files. 
#Use popation density to create a colour coded map based on population density
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Country:
    """A class used to create a Country object.

        Attributes:
            name (str): String that represents the country's name
            average (int): Integer that represents the average population from 2000 to 2020
            minimum (int): Integer that represent the smallest population value of Country between 2000 and 2020
            maximum (int): Integer that represent the largest population value of Country between 2000 and 2020
    """

    def __init__(self, name, average, minimum, maximum):
        self.name = name
        self.average = average
        self.minimum = minimum
        self.maximum = maximum
        

    def print_name(self):
        """A function that prints the country name from counntry instance.
        
        Parameters: None
        Return: None
        
        """
        print(f"\n***Country selected is {self.name}***\n")

    def print_average_pop(self):
        """A function that prints the average population of country instance.

        Parameters: None
        Return: None

        """
        print(f"Average Population of {self.name} from 2000 to 2020: {self.average:.0f} people")
    
    def print_minimum_pop(self):
        """A function that prints the minimum population of country instance.

        Parameters: None
        Return: None

        """
        print(f"Minimum Population of {self.name} was: {self.minimum:.0f} people")
    
    def print_maximum_pop(self):
        """A function that prints the maximum population of country instance.

        Parameters: None
        Return: None

        """
        print(f"Maximum Population of {self.name} was: {self.maximum:.0f} people")

class UN_Region:
    """A class used to create a UN Region object.

        Attributes:
            name (str): String that represents the name of the UN Region
            average (int): Integer that represents the average size of countries in UN Region
            minimum (int): Integer that represents the smallest country size in UN Region
            maximum (int): Integer that represents the largest country size in UN Region
    """

    def __init__(self, name, average, minimum, maximum):
        self.name = name
        self.average = average
        self.minimum = minimum
        self.maximum = maximum
        

    def print_name(self):
        """A function that prints the UN Region name from UN_Region instance.
        
        Parameters: None
        Return: None
        
        """
        print(f"\n***UN Region selected is {self.name}***\n")

    def print_average_size(self):
        """A function that prints the average size of countries in UN_Region instance.

        Parameters: None
        Return: None

        """
        print(f"Average size of countries in {self.name} is {self.average:.0f} square kilometers.")
    
    def print_minimum_size(self):
        """A function that prints the smallest country size in UN_Region instance.

        Parameters: None
        Return: None

        """
        print(f"The smallest country size in {self.name} was {self.minimum:.0f} square kilometers")
    
    def print_maximum_size(self):
        """A function that prints the largest country size in UN_Region instance.

        Parameters: None
        Return: None

        """
        print(f"The largest country size in {self.name} was {self.maximum:.0f} square kilometers")

class UN_Sub_Region:
    """A class used to create a UN Sub-Region object.

        Attributes:
            name (str): String that represents the name of the UN Sub-Region
            average (int): Integer that represents the average size of countries in UN Sub-Region
            minimum (int): Integer that represents the smallest country size in UN Sub-Region
            maximum (int): Integer that represents the largest country size in UN Sub-Region
    """

    def __init__(self, name, average, minimum, maximum):
        self.name = name
        self.average = average
        self.minimum = minimum
        self.maximum = maximum
        

    def print_name(self):
        """A function that prints the UN Sub-Region name from UN_Sub_Region instance.
        
        Parameters: None
        Return: None
        
        """
        print(f"\n***UN Sub-Region selected is {self.name}***\n")

    def print_average_size(self):
        """A function that prints the average size of countries in UN_Sub_Region instance.

        Parameters: None
        Return: None

        """
        print(f"Average size of countries in {self.name} is {self.average:.0f} square kilometers.")
    
    def print_minimum_size(self):
        """A function that prints the smallest country size in UN_Sub_Region instance.

        Parameters: None
        Return: None

        """
        print(f"The smallest country size in {self.name} was {self.minimum:.0f} square kilometers")
    
    def print_maximum_size(self):
        """A function that prints the largest country size in UN_SUb_Region instance.

        Parameters: None
        Return: None

        """
        print(f"The largest country size in {self.name} was {self.maximum:.0f} square kilometers")

class Threatened_species:
    """A class used to create a Threatened_species object.

        Attributes:
            name (str): String that represents the name of the country 
            average (int): Integer that represents the average number of endagered species in the country 
            minimum (int): Integer that represents the smallest number of endagered species in the country
            maximum (int): Integer that represents the largest number of endagered species in the country 
    """

    def __init__(self, name, average, minimum, maximum):
        self.name = name
        self.average = average
        self.minimum = minimum
        self.maximum = maximum
        

    def print_average_threatened(self):
        """A function that prints the average number of threatened species in Threatened_species instance.

        Parameters: None
        Return: None

        """
        print(f"Average number of threatened species in {self.name} is {self.average:.0f} species")
    
    def print_minimum_threatened(self):
        """A function that prints the smallest number of threatened species in Threatened_species instance.

        Parameters: None
        Return: None

        """
        print(f"The smallest number of threatened species in {self.name} is {self.minimum:.0f} species")
    
    def print_maximum_threatened(self):
        """A function that prints the largest number of threatened species in Threatened_species instance.

        Parameters: None
        Return: None

        """
        print(f"The largest number of threatened species in {self.name} is {self.maximum:.0f} species")



def main():
    #Import data 
    country_data = pd.read_csv('Country_Data.csv', index_col='Country')
    population_data = pd.read_csv('Population_Data.csv', index_col='Country')
    species_data = pd.read_csv('Threatened_Species.csv', index_col='Country')

    
    main_run = True
    while main_run == True:
        print('----------------------------------------------------------------------------------------')
        print('|    Welcome to the main menu...')
        print('|    This program can be used to lookup and display statistics calculated from multiple data files')
        print('|')
        print('|    If you wish to terminate the program please input "0"...')
        print('|')
        print('|    Please choose one of the following categories to display statitics associated with your choice:')
        print('|        1 : Country Name')
        print('|        2 : UN Region')
        print('|        3 : UN Sub-Region')
        print('----------------------------------------------------------------------------------------')
        #Ask for category input
        while True:
            try:
                category = int(input())
            except ValueError:
                print('Invalid input. Please enter the number associated with the choice you would like to make:')
                continue
            else:
                break

        while category > 3 or category < 0: #verify that input is valid
            print('Invalid input. Please enter the number associated with the choice you would like to make:')
            category = int(input())
        
        if category == 1:
            country_name = input('Please input country name:\n').title() 
            countries_list = population_data.index.tolist()

            while True:         #verify that input is valid(apart of list) using while loop
                if country_name in countries_list:   
                    break   
                else:
                    print('You must enter a valid country name.')
                    country_name = input('Please input country name:\n').title()

            #Create numpy array based on country_name(user input)
            country_name_data = pd.DataFrame(population_data.loc[country_name])
            country_name_array = np.array(country_name_data)

            #Calculate mean min and max
            minimum_pop_array = np.amin(a= country_name_array, axis = 0)
            minimum_pop = minimum_pop_array[0]
            maximum_pop_array = np.amax(a= country_name_array, axis = 0)
            maximum_pop = maximum_pop_array[0]
        
            average_pop_array = np.mean(a= country_name_array, axis=0)
            average_pop = average_pop_array[0]

            #initalize Country class
            Country.__init__(Country, country_name, average_pop, minimum_pop, maximum_pop) 
            Country.print_name(Country)

            #Create numpy array based on country_name(user input)
            threatened_species_data = pd.DataFrame(species_data.loc[country_name])
            threatened_species_array = np.array(threatened_species_data)
            
            minimum_threatened_species = np.min(threatened_species_array)
            maximum_threatened_species = np.max(threatened_species_array)
            average_threatened_species = np.mean(threatened_species_array)

            #intitalize Threatened_species class
            Threatened_species.__init__(Threatened_species, country_name, average_threatened_species, minimum_threatened_species, maximum_threatened_species)
            
            #print(threatened_species_data)
            #display country name stat options
            print('-------------------------------------------------------------')
            print('|     The following functions are available:')
            print(f'|         1 : Calculate average population of {country_name}')
            print(f'|         2 : Calculate minimum population of {country_name}')
            print(f'|         3 : Calculate maximum population of {country_name}')
            print(f'|         4 : Calculate average of endangered species in {country_name}')
            print(f'|         5 : Calculate smallest number of endagered species in {country_name}')
            print(f'|         6 : Calculate largest number of endagered species in {country_name}')
            print('-------------------------------------------------------------') 
            #Ask for second input
            while True:
                try:
                    second_user_input = int(input('Please enter corrisponding number to access statistics from above: '))
                except ValueError:
                    print('Invalid input. Please enter the number associated with the choice you would like to make:')
                    continue
                else:
                    break
            #validate second user input
            while 6 < second_user_input or second_user_input < 1 :
                second_user_input = int(input('Invalid input.\nPlease select a number between 1 and 3: '))

            if second_user_input == 1:
                #Print average population for input country 
                Country.print_average_pop(Country)
            elif second_user_input == 2:
                #Print min population for input country 
                Country.print_minimum_pop(Country)
            elif second_user_input ==3:
                #Print max population for input country
                Country.print_maximum_pop(Country)
            elif second_user_input == 4:
                #Print average number of threatened species for input country 
                Threatened_species.print_average_threatened(Threatened_species)
            elif second_user_input == 5:
                #Print minumum number of threatened species for input country 
                Threatened_species.print_minimum_threatened(Threatened_species)
            elif second_user_input == 6:
                #Print maximum number of threatened species for input country
                Threatened_species.print_maximum_threatened(Threatened_species) 

            
            
            plot_data = input('\nWould you like to plot this data? (y/n): ')
            
            while True:
                if plot_data not in ('y', 'n'):
                    plot_data = input('\nInvalid input. Please input "y" or "n": ')
                else:
                    break
            
            mean_pop_array = [average_pop_array] * len(population_data.columns)
            
            if plot_data == 'y':
                if 1 <= second_user_input <= 3:
                    plt.plot(population_data.columns, country_name_array, label = f'{country_name}')
                    plt.plot(population_data.columns, mean_pop_array, '--', label = 'Average', color = 'red')
                    plt.title(f'{country_name}\'s Population From 2000 to 2020', fontsize =16)
                    plt.xlabel('Time (Years)', fontsize = 11.5)
                    plt.ylabel('Population', fontsize = 11.5)
                    plt.xticks(rotation = 60)
                    plt.grid(color='silver', linewidth=0.5, which='both')
                    plt.grid(which = 'minor', alpha = 0.2)
                    plt.grid(which = 'major', alpha = 0.5)
                    plt.subplots_adjust(left=0.1,bottom=0.143,right=0.962,top=0.924)
                    plt.legend(shadow = True)
                    plt.ticklabel_format(axis="y", style="plain")
                    plt.margins(x=0)
                    plt.show()
                elif 3 < second_user_input <=6:
                    x_label = np.array(species_data.columns.values)
                    y_axis = np.array(threatened_species_data.squeeze())
                    def absolute_value(val):
                        """A function that prints the number of each species for a country.

                            Parameters: None
                            Return: number of species

                        """
                        percent_species  = np.round(val/100.*y_axis.sum(), 0)
                        number_species = int(percent_species)
                        return number_species
                    plt.pie(y_axis, labels = x_label, autopct= absolute_value, explode = (y_axis == max(y_axis))*0.1, startangle= 180)
                    plt.legend(shadow= True)
                    plt.title(f'Threatened Species Data for {country_name}')
                    plt.show()
            elif plot_data == 'n':
                print('Your calculation are displayed above, you may continue to use the program...')

        elif category == 2:
            un_region = input('Please input UN Region:\n').title()
            un_region_list = country_data['UN Region'].tolist()

            while True:         #verify that input is valid(apart of list) 
                if un_region in un_region_list:   
                    break   
                else:
                    print('You must enter a valid UN Region.')
                    un_region = input('Please input UN Region:\n').title()
            
            #Create numpy array based on user input 
            sq_km_data = country_data[country_data['UN Region'] == un_region]
            sq_km_array = sq_km_data['Sq Km'].to_numpy()
            #Calculate mean min and max
            minimum_size = np.min(sq_km_array) 
            maximum_size = np.max(sq_km_array)
            average_size = np.mean(sq_km_array)
            
            #initalize UN_Region Class
            UN_Region.__init__(UN_Region, un_region, average_size, minimum_size, maximum_size) 
            UN_Region.print_name(UN_Region)
            
            
            #display UN Region stat options
            print('-------------------------------------------------------------')
            print('|     The following functions are available:')
            print(f'|         1 : Calculate average size of countries in {un_region} in square kilometers')
            print(f'|         2 : Calculate smallest country size in {un_region} in square kilometers')
            print(f'|         3 : Calculate largest country size in {un_region} in square kilometers')
            print('-------------------------------------------------------------') 
            #Ask for second input
            while True:
                try:
                    second_user_input = int(input('Please enter corrisponding number to access statistics from above: '))
                except ValueError:
                    print('Invalid input. Please enter the number associated with the choice you would like to make:')
                    continue
                else:
                    break
            #validate second user input
            while 0 > second_user_input or second_user_input > 3:
                second_user_input = int(input('Invalid input.\nPlease select a number between 1 and 3: '))
            
            if second_user_input == 1:
                #Print average size for countries in UN Region
                UN_Region.print_average_size(UN_Region)
            elif second_user_input == 2:
                #Print smallest country size in UN Region 
                UN_Region.print_minimum_size(UN_Region)
            elif second_user_input == 3:
                #Print largest country size in UN Region 
                UN_Region.print_maximum_size(UN_Region)

            #plot data 
            plot_data = input('\nWould you like to plot this data? (y/n): ')
            while True:
                if plot_data not in ('y', 'n'):
                    plot_data = input('\nInvalid input. Please input "y" or "n": ')
                else:
                    break
           #using mathplotlib creates a visual representation of the data 
            if plot_data == 'y':
                y_axis = sq_km_data['Sq Km']
                x_axis = sq_km_data.index 
                plt.title(f'Size of Countries in {un_region}', fontsize= 16)
                plt.ylabel('Countries', fontsize =11.5 )
                plt.xlabel('Square Km(Km²)', fontsize =11.5)
                plt.barh(x_axis, y_axis, label = 'Sq Km', color = 'royalblue')
                plt.legend(shadow= True)
                plt.grid(color='silver', linewidth=0.5, axis='both', alpha=0.5)# added to make graphs easier to read
                plt.subplots_adjust(left=0.152, bottom=0.076,top=0.907,right=0.966)
                plt.ticklabel_format(axis="x", style="plain")
                plt.margins(y=0)
                plt.show()
            elif plot_data == 'n':
                print('Your calculation are displayed above, you may continue to use the program...')

        elif category == 3:
            un_subregion = input('Please input UN Sub-Region:\n').title()
            un_subregion_list = country_data['UN Sub-Region'].tolist()

            while True:         #verify that input is valid(apart of list) 
                if un_subregion in un_subregion_list:   
                    break   
                else:
                    print('You must enter a valid UN Sub-Region.')
                    un_subregion = input('Please input UN Sub-Region:\n').title()
            
            #Create numpy array based on user input
            un_subregion_data = country_data[country_data['UN Sub-Region'] == un_subregion]
            un_subregion_array = un_subregion_data['Sq Km'].to_numpy()
            # uses numpy to find min max and mean 
            minimum_size = np.amin(a= un_subregion_array)
            maximum_size = np.amax(a= un_subregion_array)
            average_size = np.mean(a= un_subregion_array)
            
            #initalize UN_Sub_Region Class
            UN_Sub_Region.__init__(UN_Sub_Region, un_subregion, average_size, minimum_size, maximum_size) 
            UN_Sub_Region.print_name(UN_Sub_Region)

            #display UN Sub-Region stat options
            print('-------------------------------------------------------------')
            print('|     The following functions are available:')
            print(f'|         1 : Calculate average size of countries in {un_subregion} in square kilometers')
            print(f'|         2 : Calculate smallest country size in {un_subregion} in square kilometers')
            print(f'|         3 : Calculate largest country size in {un_subregion} in square kilometers')
            print('-------------------------------------------------------------') 
            #Ask for second input
            while True:
                try:
                    second_user_input = int(input('Please enter corrisponding number to access statistics from above: '))
                except ValueError:
                    print('Invalid input. Please enter the number associated with the choice you would like to make:')
                    continue
                else:
                    break
            #validate second user input
            while 0 > second_user_input or second_user_input > 3:
                second_user_input = int(input('Invalid input.\nPlease select a number between 1 and 3: '))
            
            if second_user_input == 1:
                #Print average size for countries in UN Region
                UN_Sub_Region.print_average_size(UN_Sub_Region)
            elif second_user_input == 2:
                #Print smallest country size in UN Region 
                UN_Sub_Region.print_minimum_size(UN_Sub_Region)
            elif second_user_input == 3:
                #Print largest country size in UN Region 
                UN_Sub_Region.print_maximum_size(UN_Sub_Region)

            #plot here 
            plot_data = input('\nWould you like to plot this data? (y/n):')
            while True:
                if plot_data not in ('y', 'n'):
                    plot_data = input('\nInvalid input. Please input "y" or "n": ')
                else:
                    break
            # creates a visuale represention of data based on users input 
            if plot_data == 'y':
                y_axis = un_subregion_data['Sq Km']
                x_axis = un_subregion_data.index
                plt.title(f'Size of Countries in {un_subregion}', fontsize = 20)
                plt.xlabel('Square Km(Km²)', fontsize = 16)
                plt.ylabel('Countries', fontsize = 16)
                plt.barh(x_axis, y_axis,align = 'center', color = 'orange', label = 'Sq Km')
                plt.legend(shadow= True)
                plt.grid(color='silver', linewidth=0.5, axis='both', alpha=0.5)
                plt.ticklabel_format(axis="x", style="plain")
                plt.subplots_adjust(left=0.18, bottom=0.076,top=0.907,right=0.966)
                plt.margins(y=0)

                plt.show()
            elif plot_data == 'n':
                print('Your calculation are displayed above, you may continue to use the program...')
            
        if category == 0:
            main_run = False
            print('***Program Terminated***')
            print('----------------------------------------------')

if __name__ == '__main__':
    main()