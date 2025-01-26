// Place const infront of function making return type const 
// Pass container by reference to avoid making copies of it

template <typename T> //Old school equivalent: template <class T>
const long double KahanSum(T & MyContainer)
{
    long double MySum = 0.0;
    long double accumulator = 0.0; 
    
    for (typename T::iterator it = MyContainer.begin(); it != MyContainer.end(); ++it) 
        {
            if(*MyContainer.begin() < 0)
            { // bounds checking
                std::cout << "please start the iterator at the first index of the container." << std::endl;
                long double check = -1.0;
                return check;
            }
            //std::cout << "In my iterator:" << *it << std::endl;
            std::cout.precision(17);
            long double precision = *it - accumulator;
            long double t = MySum + precision; 
            accumulator = (t - MySum) - precision;
            MySum = t;
        }
    return MySum;
}

template <typename T>
const long double RegularSum(T &MyContainer)
{
    long double MySum = 0.0;
    long double accumulator = 0.0; 
    
    for (typename T::iterator it = MyContainer.begin(); it != MyContainer.end(); ++it) 
        {
            if(*MyContainer.begin() < 0)
            { // bounds checking
                std::cout << "please start the iterator at the first index of the container." << std::endl;
            }
            //std::cout << "In my iterator:" << *it << std::endl;
            std::cout.precision(17);
            MySum += *it;
        }
    return MySum;
}

//g++ -std=c++17 main.cpp KahanSum.cpp -o testing