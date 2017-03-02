

class AbstractParser(object):
    def __init__(self, scanner):
        self.scanner = scanner
    def __getattr__(self, name):
        return getattr(self.scanner, name)

class ExpressionPArser(AbstractParser):
    def expr(self):
        ...
        token = self.next_token()
        ...
        self.push_back(token)

"""
If without the AbstractParser --> bridge;

it will be 
    --> self.scanner.next_token()
    --> self.scanner.push_back(token) 
"""


###############################################################################



#===================================================================
"""
Below is an example of bridge, extracted from github
https://gist.github.com/pazdera/1173009

*unsure of its validity with the above description
"""
#===================================================================



# Example of `bridge' design pattern
# This code is part of http://wp.me/p1Fz60-8y
# Copyright (C) 2011 Radek Pazdera

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


class AbstractInterface:

    """ Target interface.
    This is the target interface, that clients use.
    """

    def some_functionality(self):
        raise NotImplemented()


class Bridge(AbstractInterface):

    """ Bridge class.
    
    This class forms a bridge between the target
    interface and background implementation.
    """

    def __init__(self):
        self.__implementation = None


class UseCase1(Bridge):

    """ Variant of the target interface.
    This is a variant of the target Abstract interface.
    It can do something little differently and it can
    also use various background implementations through
    the bridge.
    """

    def __init__(self, implementation):
        self.__implementation = implementation

    def some_functionality(self):
        print "UseCase1: ",
        self.__implementation.another_functionality()


class UseCase2(Bridge):
    def __init__(self, implementation):
        self.__implementation = implementation

    def some_functionality(self):
        print "UseCase2: ",
        self.__implementation.another_functionality()


class ImplementationInterface:
    
    """ Interface for the background implementation.
    This class defines how the Bridge communicates
    with various background implementations.
    """

    def another_functionality(self):
        raise NotImplemented

class Linux(ImplementationInterface):

    """ Concrete background implementation.
    A variant of background implementation, in this
    case for Linux!
    """

    def another_functionality(self):
        print "Linux!"


class Windows(ImplementationInterface):
    def another_functionality(self):
        print "Windows."

"""
Notes: 
    - <some_functionality> is a generalized function that internally calls the <another_functionality> of the implementation interface
    - it wraps up all the additional code needed to run, before calling <another_functionality> 
            --> print "UseCase1: "
            --> print "UseCase2: ",
"""


def main():
    linux = Linux()
    windows = Windows()

    # Couple of variants under a couple
    # of operating systems.
    useCase = UseCase1(linux)
    useCase.some_functionality()

    useCase = UseCase1(windows)
    useCase.some_functionality()

    useCase = UseCase2(linux)
    useCase.some_functionality()

    useCase = UseCase2(windows)
    useCase.some_functionality()


if __name__ == "__main__":
    main()