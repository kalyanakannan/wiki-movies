import requests
import numpy as np
import wikitextparser as wtp

class Api:
    
    def __init__(self):
        self.BaseUrl = "https://www.wikipedia.org/w/api.php"
        self.request = requests.Session()
        self.separate = 10
        self.format = 'json'
        self.params = {}
        self.eicontinue = ""

    def setFormat(self, format='json'):
        """set respone format for the api

        Args:
            format (str, optional): _description_. Defaults to 'json'.
        """
        self.params['format'] = format

    def setContinue(self, eicontinue):
        """ set params for next set of data

        Args:
            eicontinue (_string_): _description_
        """
        self.eicontinue = eicontinue

    def getContinue(self):
        """ return continue value for api

        Returns:
            _type_: _description_
        """
        return self.eicontinue

    def setPosterParams(self):
        """_summary_
        """
        self.params = {
            "action": "query",
            "pilicense":"any",
            "prop":"pageimages|pageterms",
            "piprop":"original"

        }

    def setPageDetailsParams(self):
        """_summary_
        """
        self.params = {
            "action": "query",
            "prop":"revisions",
            "rvsection": "0",
            "rvprop":"content"
        }

    def getPageDetails(self, page_ids):
        """_summary_

        Args:
            page_ids (_type_): _description_

        Returns:
            _type_: _description_
        """
        if(not(page_ids)):
            raise Exception("page_ids is empty")

        self.setPageDetailsParams()
        self.setPageIds(page_ids)
        self.setFormat()
        response = self.request.get(url=self.BaseUrl, params=self.params).json()
        page_details = response["query"]["pages"]
        return page_details

    def getPosters(self,page_ids):
        """_summary_

        Args:
            page_ids (_type_): _description_

        Returns:
            _type_: _description_
        """
        if(not(page_ids)):
            raise Exception("page_ids is empty")

        self.setPosterParams()
        self.setPageIds(page_ids)
        self.setFormat()
        poster_details = self.request.get(url=self.BaseUrl, params=self.params).json()
        return poster_details["query"]["pages"]
        

    def getPageIds(self, movies):
        """_summary_

        Args:
            movies (_type_): _description_

        Returns:
            _type_: _description_
        """
        if(not(movies)):
            raise Exception("movies is empty")
            
        pageIds =[str(movie.get('pageid')) for movie in movies]
        splited_lists = np.array_split(np.array(pageIds), self.separate)
        return splited_lists

    def getTitles(self,movies):
        """_summary_

        Args:
            movies (_type_): _description_

        Returns:
            _type_: _description_
        """
        if(not(movies)):
            raise Exception("movies is empty")

        return [str(movie.get('title')) for movie in movies]

    def mergePageIds(self, pageIds):
        """_summary_

        Args:
            pageIds (_type_): _description_

        Returns:
            _type_: _description_
        """
        # if(not pageIds)=):
        #     raise Exception("pageIds is empty")

        return "|".join(pageIds)

    def setPageIds(self,pageIds):
        """_summary_

        Args:
            pageIds (_type_): _description_
        """
        if(not(pageIds)):
            raise Exception("pageIds is empty")

        self.params['pageids'] = pageIds

    def formatAttributeByPageId(self, attributes, page_id):
        """_summary_

        Args:
            attributes (_type_): _description_
            page_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        if(not(attributes)):
            raise Exception("infobox name is empty")
        if(not(page_id)):
            raise Exception("page_id is empty")

        details = {}
        details["page_id"] = page_id
        for attribute in attributes:
            details[attribute.name.strip()] = attribute.value.strip()
        return details

    def extractTemplateAttributeByPageId(self, text,Infobox_name, page_id) -> dict:
        """extract attributes based on template info box name and page id

        Args:
            text (str): wiki text
            template_name (str): info box name
            page_id (str): page id of wiki

        Returns:
            dict: attributes
        """
        if(not(Infobox_name)):
            raise Exception("infobox name is empty")
        if(not(page_id)):
            raise Exception("page_id is empty")
        parsed = wtp.parse(text)
        index = 0
        for template in parsed.templates:
            template.name.strip()
            if template.name.strip() == Infobox_name:
                return self.formatAttributeByPageId(parsed.templates[index].arguments, page_id)
            index = index + 1
        return []