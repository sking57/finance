// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <string.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Represents a hash table
node *hashtable[N];

//define global variable for how many words from dictionary are sorted (will help with size)
int counter = 0;

// Hashes word to a number between 0 and 26, inclusive, based on its first letter.
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        // allocate memory for new node
        node *new_node  = malloc(sizeof(node));
        node *head = hashtable[hash(word)];

        // unload dictionary and stop program if the new node points to nothing (this happens when we run out of space)
        if (new_node == NULL)
        {
            unload();
            return false;
        }
        // when new_node does exist, copy each word from the dictionary into a node
        strcpy(new_node->word, word);

        // make linked list while making sure we don’t lose information/nodes in our linked list
        new_node->next = head;

        // assign each word to a bucket
        hashtable[hash(word)] = new_node;

        // keep track of how many words are sorted
        counter ++;
    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // counter will denote how many words were sorted!
    return counter;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // find word in hash table, point cursor to it to initialize
    node *cursor = hashtable[hash(word)];

    // traversing linked lists with cursor
    while (cursor != NULL)
    {
        // compare two strings
        int check = strcasecmp(cursor->word, word);
        if (check == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int k = 0; k < N; k++)
    {
        node *cursor2 = hashtable[k];
        while (cursor2 != NULL)
        {
            node *temp = cursor2;
            cursor2 = cursor2->next;
            free(temp);
        }
    }
    return true;
}
