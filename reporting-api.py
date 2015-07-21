import webapp2
from datamodels import Employees
from magimetrics import APIHandler, api_key_required


class GetListOfTables(APIHandler):
    @api_key_required
    def get(self):
        self.render_json({"tables": [{"tablename": "Employees", "tablehash": "employees"}], "error": False})


class GetTable(APIHandler):
    @api_key_required
    def get(self):
        if self.request.get("tablehash") == "employees":
            list_of_fields = [{"identifier": "employee", "label": "Employee", "type": "text"},
                              {"identifier": "tps_reports", "label": "TPS Reports", "type": "number"}]
            list_of_rows = []
            employees = Employees.query().fetch()
            for employee in employees:
                list_of_rows.append({"employee": employee.name, "tps_reports": employee.tps_reports})
            self.render_json({"table": {"fields": list_of_fields, "rows": list_of_rows}, "error": False})
        else:
            self.render_error("The requested table was not found.")


app = webapp2.WSGIApplication([
    ('/reporting-api/get-list-of-tables/', GetListOfTables),
    ('/reporting-api/get-table/', GetTable)
], debug=False, config=None)
