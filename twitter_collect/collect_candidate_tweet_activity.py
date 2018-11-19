import tweepy

def get_candidate_queries(num_candidate, file_path,file_type):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    queries=[]

    keywords_file_path="{}_{}_candidate_{}.txt".format(file_path,file_type,num_candidate)
    try:
        with open(keywords_file_path,'r') as keyword_file: #lit le fichier texte
            keywords=keyword_file.read().split("\n")    #découpe le fichier des keywords en liste selon les retours a la ligne

        i=0
        for keyword1 in keywords:
            if file_type == "hashtag":
                queries.append("#{}".format(keyword1))
            else:
                queries.append("{}".format(keyword1))
            if i <len(keywords)-2:
                for keyword2 in keywords[i+1:]:
                    if file_type == "hashtag":
                        queries.append("#{} AND #{}".format(keyword2, keyword2))
                    else:
                        queries.append("{} AND {}".format(keyword2, keyword2))
            i = i + 1

        return queries

    except IOError:
        print("file {} is missing.".format(keywords_file_path))
        return []
